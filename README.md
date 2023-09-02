# Chat Template Formatter Utility
Author: Yogesh Baghel
## Overview
This utility function is designed to format text into structured chat templates using specific handlebars tags. It can be used to prepare chat templates for various applications.
## Usage

Follow these steps to use the utility function:

1. Clone the Repository:

   Clone this repository to your local machine.

   ```bash
   git clone https://github.com/yogesh-hack/chat-template-formatter.git
   ```

2. Navigate to the Project Directory:

   Change the current directory to the project folder.

   ```bash
   cd chat-template-formatter
   ```

3. Install Dependencies:

   Install the required dependencies for the utility function. We use pyparsing for text parsing.

   ```bash
   pip install pyparsing
   ```

4. Use the Utility Function:

   Use the `format_chat_template` function from the provided Python script to format your chat templates.

   ```python
   from chat_formatter import format_chat_template

   input_text = "Your input chat template here"
   formatted_text = format_chat_template(input_text)

   print(formatted_text)
   ```

5. Run the Script:

   Execute your Python script that uses the `format_chat_template` function with your chat templates as input.

6. Verify the Output:

   Verify that the output matches the expected formatted chat template.

## Examples

Here are some examples of using the utility function:

```python
input_text = "how are things going, tell me about Delhi"
formatted_text = format_chat_template(input_text)
print(formatted_text)
```

```python
input_text = "Tweak this proverb to apply to model instructions instead. Where there is no guidance{{gen 'rewrite'}}"
formatted_text = format_chat_template(input_text)
print(formatted_text)
```
