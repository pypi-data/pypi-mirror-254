# ymlconf

## What is it for?

Using YAML configuration files for python require less boilerplate code, and accessing the values by dot notation.

## Installation

```bash
pip install comfyconf
```

## Usage

### Basic

Create a config file in YAML and name it foo.yaml:

```yaml

test:
  title: 'test' 
  ip: '127.0.0.1' 
  port: 5000

production:
  title: 'My amazing server' 
  ip: '1234.255.255.1' 
  port: 1234
```

Now, load it using `make_config`:

```python
>>> from comfyconf import make_config   
>>> config = make_config('foo.yaml')
>>> config.test.ip
'127.0.0.1'
>>> config.production.port
1234  
```

Note that numerical keys are not allowed (even if they're strings in YAML), doing so will raise a `ValueError` 

### Using ruamel.yaml as parser instead of pyyaml

If you prefer ruamel.yaml or need to parse YAML 1.2 document you can use:

```python 
>>> config = make_config('foo.yaml', reader='ruamel')
```

## Contribute

If you find a bug or have a feature request, please raise on issue on [Github](https://github.com/edager/comfyconf/issues). 

Contributions are more than welcome, but please:

 1. Write unittest (pytest) 
 2. Write Numpy styled docstrings     
