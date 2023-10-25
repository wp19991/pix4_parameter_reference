import json

with open('px4参数_翻译.json', 'r', encoding='utf-8') as f:
    px4_data = json.loads(''.join(f.readlines()))

print(len(px4_data))

readme_str = '''# pix4_parameter_reference
> 使用gpt翻译pix4的参数，并且加上gpt的解释

> https://docs.px4.io/main/zh/advanced_config/parameter_reference.html

'''

for i,t_data in enumerate(px4_data):
    t_str = f'''{i+1}. {t_data['名称']}
- 名称：{t_data['名称']}
- 参数描述：{t_data['参数描述']}
  - 翻译：{t_data.get('翻译', {'参数描述': '', '注解': ''}).get('参数描述', '')}
  - gpt注解：{t_data.get('翻译', {'参数描述': '', '注解': ''}).get('注解', '')}
- `[Min, Max]`：`{t_data['[Min, Max] (Incr.)']}`
- 默认值：`{t_data['默认值']}`
- 单位：`{t_data['单位']}`


'''
    print(t_str)
    readme_str += t_str

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_str)
