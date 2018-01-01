# Contributing to Community


The following is a set of guidelines for contributing to Community. These are mostly guidelines, so make sure to use your best judgment.


### Adding Features

When adding features, be sure to keep the original [specification](https://docs.google.com/document/d/1Mn8p3v4KKbJacjeAZeycCwP7lKkC2MIVJVUWuMc_bzk/edit?usp=sharing) in mind at all times.


### Bugs

Bugs are tracked as [GitHub issues](https://guides.github.com/features/issues/). Create an issue and try to provide the following information:

Explain the problem and include additional details:

* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem** in as many details as possible. 
* **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
* **Explain which behavior you expected to see instead and why.**
* **Include screenshots and animated GIFs** which show you following the described steps and clearly demonstrate the problem. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.

Provide more context by answering these questions:

* **Did the problem start happening recently** (e.g. after a recent commit) or was this always a problem?
* If the problem started happening recently, **can you reproduce the problem in an earlier branch?** What's the most recent version in which the problem doesn't happen?
* **Can you reliably reproduce the issue?** If not, provide details about how often the problem happens and under which conditions it normally happens.
* Include details about your configuration and environment


## Styleguides


### Git Commit Messages
* Describe your changes in present tense, imperative mood. 
From the [Git documentation](https://git.kernel.org/pub/scm/git/git.git/tree/Documentation/SubmittingPatches?id=HEAD#n133): 
> "make xyzzy do frotz" instead of "[This patch] makes xyzzy do frotz" or "[I] changed xyzzy to do frotz", as if you are giving orders to the codebase to change its behavior.
* Be descriptive ("Fix issue with x regarding y" not "Fix bug")
* Elaborate beyond the title
* Limit the first line to 72 characters or less
* Always reference issues
* Reference issues after the first line



### Python

All Python code must adhere to [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/).

* Yes:
 ```python
# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# More indentation included to distinguish this from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```
* No:

```python
# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
  ```



### JavaScript

All JavaScript must adhere to [JavaScript Standard Style](https://standardjs.com/).

* 2 spaces – for indentation
* Single quotes for strings – except to avoid escaping
* No semicolons
* Never start a line with   `(`, `[`, or ``` ` ```
* Space after keywords 

```js
if (condition) { ... }
```

* Space after function name 

```js
functionName (arg) { ... } 
```

* Always use ` === ` instead of ` == – ` but ` obj == null ` is allowed to check `null || undefined`
* Always prefix browser globals with window – except document and navigator are okay



### HTML/CSS
When in doubt, please refer to the [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html)
