import json
from jinja2 import Environment, FileSystemLoader
from openapi_core import Spec
from example.example import app


openapi = app.openapi()

with open('example/example.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(openapi, indent=2))


def schema_links(ref):
    if ref:
        for key, value in ref.items():
            if key == '$ref':
                schema = value.split('/')[-1]
                return f"[{schema}](#{schema.lower()})"
            elif key == 'type':
                return f"{value}"
            else:
                return ''
            

def json_dumps(data):
    return json.dumps(data, indent=2)


spec = Spec.from_dict(openapi)
env = Environment(loader=FileSystemLoader('templates'))
env.filters['schema_links'] = schema_links
env.filters['json_dumps'] = json_dumps
template = env.get_template('template.md.jinja2')
rendered = template.render(spec=spec)
with open('example/example.md', 'w', encoding='utf-8') as file:
    file.write(rendered)