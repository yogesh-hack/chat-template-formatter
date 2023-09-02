import pyparsing as pp

def format_chat_template(input_text):
    # Define pyparsing grammar
    user_tag_open = pp.Literal('{{#user}}')
    user_tag_close = pp.Literal('{{/user}}')
    assistant_tag_open = pp.Literal('{{#assistant}}')
    assistant_tag_close = pp.Literal('{{/assistant}}')
    gen_command = pp.Literal('{{gen') + pp.SkipTo('}}', include=True) + pp.Literal('}}')

    # Define a callback function to wrap text in tags
    def wrap_user_tag(tokens):
        return '{{#user}}' + tokens[0] + '{{/user}}'

    def wrap_assistant_tag(tokens):
        return '{{#assistant}}' + tokens[0] + '{{/assistant}}'

    # Define the overall grammar for the template
    template_grammar = (
        pp.Optional(assistant_tag_open + gen_command + assistant_tag_close).setParseAction(wrap_assistant_tag) |
        pp.SkipTo(assistant_tag_open | pp.StringEnd(), include=True).setParseAction(wrap_user_tag)
    )

    # Parse the input text and format it
    parsed_text = template_grammar.transformString(input_text)

    # Ensure the template ends with an assistant command
    if not parsed_text.endswith('{{gen \'write\' }} {{/assistant}}'):
        parsed_text += ' {{#assistant}}{{gen \'write\' }}{{/assistant}}'

    return parsed_text

# Test cases
# if __name__ == "__main__":
#     input1 = "how are things going, tell me about Delhi"
#     output1 = format_chat_template(input1)
#     print(output1)

#     input2 = "Tweak this proverb to apply to model instructions instead. Where there is no guidance{{gen 'rewrite'}}"
#     output2 = format_chat_template(input2)
#     print(output2)
