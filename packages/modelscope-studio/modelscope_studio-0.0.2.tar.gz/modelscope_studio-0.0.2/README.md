
# `modelscope_studio`
<a href="https://pypi.org/project/modelscope_studio/" target="_blank"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/modelscope_studio"></a>  

A set of extension component, inluding components for conversational input and display in multimodal scenarios, as well as more components for vertical scenarios.

## Installation
    
```bash 
pip install modelscope_studio
```

## Usage

```python
import gradio as gr

with gr.Blocks() as demo:
    pass
if __name__ == '__main__':
    demo.launch()

```

## `Chatbot`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>value</code></td>
<td align="left" style="width: 25%;">

```python
list[
        list[
            str
            | tuple[str]
            | tuple[str | pathlib.Path, str]
            | None
        ]
    ]
    | Callable
    | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Default value to show in chatbot. If callable, the function will be called whenever the app loads to set the initial value of the component.</td>
</tr>

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.</td>
</tr>

<tr>
<td align="left"><code>every</code></td>
<td align="left" style="width: 25%;">

```python
float | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. Queue must be enabled. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute.</td>
</tr>

<tr>
<td align="left"><code>show_label</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if True, will display label.</td>
</tr>

<tr>
<td align="left"><code>container</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will place the component in a container - providing some extra padding around the border.</td>
</tr>

<tr>
<td align="left"><code>scale</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">relative width compared to adjacent Components in a Row. For example, if Component A has scale=2, and Component B has scale=1, A will be twice as wide as B. Should be an integer.</td>
</tr>

<tr>
<td align="left"><code>min_width</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>160</code></td>
<td align="left">minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will be hidden.</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.</td>
</tr>

<tr>
<td align="left"><code>height</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">height of the component in pixels.</td>
</tr>

<tr>
<td align="left"><code>rtl</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">If True, sets the direction of the rendered text to right-to-left. Default is False, which renders text left-to-right.</td>
</tr>

<tr>
<td align="left"><code>show_share_button</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">If True, will show a share icon in the corner of the component that allows user to share outputs to Hugging Face Spaces Discussions. If False, icon does not appear. If set to None (default behavior), then the icon appears if this Gradio app is launched on Spaces, but not otherwise.</td>
</tr>

<tr>
<td align="left"><code>show_copy_button</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">If True, will show a copy button for each chatbot message.</td>
</tr>

<tr>
<td align="left"><code>avatar_images</code></td>
<td align="left" style="width: 25%;">

```python
tuple[
        str | pathlib.Path | None | dict | list | tuple,
        str | pathlib.Path | None | dict | list | tuple,
    ]
    | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Tuple of two avatar image paths or URLs or dict ("avatar" and "name") or list (each item receives the previous parameters) for user(s) and bot(s) (in that order). Pass None for either the user or bot image to skip. Must be within the working directory of the Gradio app or an external URL and use `gr.update` to update.</td>
</tr>

<tr>
<td align="left"><code>avatar_image_align</code></td>
<td align="left" style="width: 25%;">

```python
"top" | "middle" | "bottom"
```

</td>
<td align="left"><code>"bottom"</code></td>
<td align="left">Aligns the avatar images to the top, middle, or bottom of the message.</td>
</tr>

<tr>
<td align="left"><code>avatar_image_width</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>45</code></td>
<td align="left">Width of the avatar image in pixels.</td>
</tr>

<tr>
<td align="left"><code>sanitize_html</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, will disable HTML sanitization for chatbot messages. This is not recommended, as it can lead to security vulnerabilities.</td>
</tr>

<tr>
<td align="left"><code>render_markdown</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, will disable Markdown rendering for chatbot messages.</td>
</tr>

<tr>
<td align="left"><code>bubble_full_width</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, the chat bubble will fit to the content of the message. If True (default), the chat bubble will be the full width of the component.</td>
</tr>

<tr>
<td align="left"><code>line_breaks</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True (default), will enable Github-flavored Markdown line breaks in chatbot messages. If False, single new lines will be ignored. Only applies if `render_markdown` is True.</td>
</tr>

<tr>
<td align="left"><code>likeable</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">Whether the chat messages display a like or dislike button. Set automatically by the .like method but has to be present in the signature for it to show up in the config.</td>
</tr>

<tr>
<td align="left"><code>layout</code></td>
<td align="left" style="width: 25%;">

```python
"panel" | "bubble" | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">If "panel", will display the chatbot in a llm style layout. If "bubble", will display the chatbot with message bubbles, with the user and bot messages on alterating sides. Will default to "bubble".</td>
</tr>

<tr>
<td align="left"><code>flushing</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True (default), will stream output the chatbot (not the user) messages to the frontend linearly when they are updated. Can be configured for each message.</td>
</tr>

<tr>
<td align="left"><code>flushing_speed</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>5</code></td>
<td align="left">Range 1 to 10, default is 5.</td>
</tr>

<tr>
<td align="left"><code>enable_base64</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">Enable base64 encoding for markdown rendering.</td>
</tr>

<tr>
<td align="left"><code>enable_latex</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will enable LaTeX rendering.</td>
</tr>

<tr>
<td align="left"><code>latex_single_dollar_delimiter</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will enable single dollar delimiter for LaTeX rendering.</td>
</tr>

<tr>
<td align="left"><code>preview</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True (default), will enable image preview.</td>
</tr>

<tr>
<td align="left"><code>llm_thinking_presets</code></td>
<td align="left" style="width: 25%;">

```python
list[dict]
```

</td>
<td align="left"><code>[]</code></td>
<td align="left">llm presets, imported from modelscope_studio.Chatbot.llm_thinking_presets .</td>
</tr>

<tr>
<td align="left"><code>data_postprocess</code></td>
<td align="left" style="width: 25%;">

```python
Callable | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>data_preprocess</code></td>
<td align="left" style="width: 25%;">

```python
Callable | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>custom_components</code></td>
<td align="left" style="width: 25%;">

```python
dict[str, CustomComponentDict] | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Define custom tags for markdown rendering.</td>
</tr>
</tbody></table>


### Events

| name | description |
|:-----|:------------|
| `change` | Triggered when the value of the Chatbot changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input. |
| `select` | Event listener for when the user selects or deselects the Chatbot. Uses event data gradio.SelectData to carry `value` referring to the label of the Chatbot, and `selected` to refer to state of the Chatbot. See EventData documentation on how to use this event data |
| `like` | This listener is triggered when the user likes/dislikes from within the Chatbot. This event has EventData of type gradio.LikeData that carries information, accessible through LikeData.index and LikeData.value. See EventData documentation on how to use this event data. |
| `flushed` |  |
| `custom` |  |



### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function. 
- When used as an output, the component only impacts the return signature of the user function. 

The code snippet below is accurate in cases where the component is used as both an input and an output.



 ```python
 def predict(
     value: list[list[MultimodalMessage | None]]
 ) -> list[
    list[
        str
        | dict
        | MultimodalInputData
        | MultimodalMessage
        | None
    ]
    | tuple
]:
     return value
 ```
 

## `Markdown`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>value</code></td>
<td align="left" style="width: 25%;">

```python
str | Callable
```

</td>
<td align="left"><code>""</code></td>
<td align="left">Value to show in Markdown component. If callable, the function will be called whenever the app loads to set the initial value of the component.</td>
</tr>

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">The label for this component. Is used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.</td>
</tr>

<tr>
<td align="left"><code>every</code></td>
<td align="left" style="width: 25%;">

```python
float | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. Queue must be enabled. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute.</td>
</tr>

<tr>
<td align="left"><code>show_label</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">This parameter has no effect.</td>
</tr>

<tr>
<td align="left"><code>rtl</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">If True, sets the direction of the rendered text to right-to-left. Default is False, which renders text left-to-right.</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.</td>
</tr>

<tr>
<td align="left"><code>sanitize_html</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, will disable HTML sanitization when converted from markdown. This is not recommended, as it can lead to security vulnerabilities.</td>
</tr>

<tr>
<td align="left"><code>line_breaks</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">If True, will enable Github-flavored Markdown line breaks in chatbot messages. If False (default), single new lines will be ignored.</td>
</tr>

<tr>
<td align="left"><code>header_links</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">If True, will automatically create anchors for headings, displaying a link icon on hover.</td>
</tr>

<tr>
<td align="left"><code>enable_base64</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">Enable base64 encoding for markdown rendering.</td>
</tr>

<tr>
<td align="left"><code>enable_latex</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will enable LaTeX rendering.</td>
</tr>

<tr>
<td align="left"><code>latex_single_dollar_delimiter</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will enable single dollar delimiter for LaTeX rendering.</td>
</tr>

<tr>
<td align="left"><code>preview</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True (default), will enable image preview.</td>
</tr>

<tr>
<td align="left"><code>data_postprocess</code></td>
<td align="left" style="width: 25%;">

```python
Callable | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>data_preprocess</code></td>
<td align="left" style="width: 25%;">

```python
Callable | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>custom_components</code></td>
<td align="left" style="width: 25%;">

```python
dict[str, CustomComponentDict] | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Define custom tags for markdown rendering.</td>
</tr>
</tbody></table>


### Events

| name | description |
|:-----|:------------|
| `change` | Triggered when the value of the Markdown changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input. |
| `custom` |  |



### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function. 
- When used as an output, the component only impacts the return signature of the user function. 

The code snippet below is accurate in cases where the component is used as both an input and an output.



 ```python
 def predict(
     value: str | None
 ) -> str | None:
     return value
 ```
 

## `MultimodalInput`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>value</code></td>
<td align="left" style="width: 25%;">

```python
MultimodalInputData | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">default text to provide in textarea. If callable, the function will be called whenever the app loads to set the initial value of the component.</td>
</tr>

<tr>
<td align="left"><code>lines</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>1</code></td>
<td align="left">minimum number of line rows to provide in textarea.</td>
</tr>

<tr>
<td align="left"><code>max_lines</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>20</code></td>
<td align="left">maximum number of line rows to provide in textarea.</td>
</tr>

<tr>
<td align="left"><code>placeholder</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">placeholder hint to provide behind textarea.</td>
</tr>

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.</td>
</tr>

<tr>
<td align="left"><code>info</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">additional component description.</td>
</tr>

<tr>
<td align="left"><code>every</code></td>
<td align="left" style="width: 25%;">

```python
float | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. Queue must be enabled. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute.</td>
</tr>

<tr>
<td align="left"><code>show_label</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if True, will display label.</td>
</tr>

<tr>
<td align="left"><code>container</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will place the component in a container - providing some extra padding around the border.</td>
</tr>

<tr>
<td align="left"><code>scale</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">relative width compared to adjacent Components in a Row. For example, if Component A has scale=2, and Component B has scale=1, A will be twice as wide as B. Should be an integer.</td>
</tr>

<tr>
<td align="left"><code>min_width</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>160</code></td>
<td align="left">minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.</td>
</tr>

<tr>
<td align="left"><code>interactive</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if True, will be rendered as an editable textbox; if False, editing will be disabled. If not provided, this is inferred based on whether the component is used as an input or output.</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will be hidden.</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>autofocus</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">If True, will focus on the textbox when the page loads. Use this carefully, as it can cause usability issues for sighted and non-sighted users.</td>
</tr>

<tr>
<td align="left"><code>autoscroll</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will automatically scroll to the bottom of the textbox when the value changes, unless the user scrolls up. If False, will not scroll to the bottom of the textbox when the value changes.</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.</td>
</tr>

<tr>
<td align="left"><code>type</code></td>
<td align="left" style="width: 25%;">

```python
"text" | "password" | "email"
```

</td>
<td align="left"><code>"text"</code></td>
<td align="left">The type of textbox. One of: 'text', 'password', 'email', Default is 'text'.</td>
</tr>

<tr>
<td align="left"><code>text_align</code></td>
<td align="left" style="width: 25%;">

```python
"left" | "right" | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">How to align the text in the textbox, can be: "left", "right", or None (default). If None, the alignment is left if `rtl` is False, or right if `rtl` is True. Can only be changed if `type` is "text".</td>
</tr>

<tr>
<td align="left"><code>rtl</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">If True and `type` is "text", sets the direction of the text to right-to-left (cursor appears on the left of the text). Default is False, which renders cursor on the right.</td>
</tr>

<tr>
<td align="left"><code>show_copy_button</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">If True, includes a copy button to copy the text in the textbox. Only applies if show_label is True.</td>
</tr>

<tr>
<td align="left"><code>data_postprocess</code></td>
<td align="left" style="width: 25%;">

```python
Callable | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>data_preprocess</code></td>
<td align="left" style="width: 25%;">

```python
Callable | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>sources</code></td>
<td align="left" style="width: 25%;">

```python
list["upload" | "microphone" | "webcam"]
```

</td>
<td align="left"><code>["upload"]</code></td>
<td align="left">A list of sources permitted. "upload" creates a upload button, "microphone" creates a microphone button. "webcam" creates a webcam button.</td>
</tr>

<tr>
<td align="left"><code>upload_button_props</code></td>
<td align="left" style="width: 25%;">

```python
dict | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">gradio UploadButton props.</td>
</tr>

<tr>
<td align="left"><code>submit_button_props</code></td>
<td align="left" style="width: 25%;">

```python
dict | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">gradio Button props.</td>
</tr>

<tr>
<td align="left"><code>file_preview_props</code></td>
<td align="left" style="width: 25%;">

```python
dict | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">FilePreview will render if `value.files` is not empty, accepting the following props: height(int).</td>
</tr>

<tr>
<td align="left"><code>webcam_props</code></td>
<td align="left" style="width: 25%;">

```python
dict | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Webcam will render if `sources` contains "webcam", accepting the following props: mirror_webcam(bool), include_audio(bool).</td>
</tr>
</tbody></table>


### Events

| name | description |
|:-----|:------------|
| `change` | Triggered when the value of the MultimodalInput changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input. |
| `input` | This listener is triggered when the user changes the value of the MultimodalInput. |
| `select` | Event listener for when the user selects or deselects the MultimodalInput. Uses event data gradio.SelectData to carry `value` referring to the label of the MultimodalInput, and `selected` to refer to state of the MultimodalInput. See EventData documentation on how to use this event data |
| `submit` | This listener is triggered when the user presses the Enter key while the MultimodalInput is focused. |
| `focus` | This listener is triggered when the MultimodalInput is focused. |
| `blur` | This listener is triggered when the MultimodalInput is unfocused/blurred. |
| `upload` | This listener is triggered when the user uploads a file into the MultimodalInput. |



### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function. 
- When used as an output, the component only impacts the return signature of the user function. 

The code snippet below is accurate in cases where the component is used as both an input and an output.



 ```python
 def predict(
     value: MultimodalInputData | None
 ) -> MultimodalInputData | dict | str | None:
     return value
 ```
 

## `MultimodalInputData`
```python
class MultimodalInputData(GradioModel):
    files: List[Union[FileData, str]] = []
    text: str
```
