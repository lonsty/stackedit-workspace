# 桌面主题：
- 需要gnome 3.20及之后版本，tweak tool

1. flat-remix-GTK-darker
    - flat-remix-GTK
2. Qogir
3. Ultimate-dark-orange

# 主题图标

- Papirus (github)

# sublime
settings
```
{
	"always_show_minimap_viewport": true,
	"bold_folder_labels": true,
	"color_scheme": "Packages/Material Theme/schemes/Material-Theme-Darker.tmTheme",
	"font_options":
	[
		"no_italic",
		"gray_antialias",
		"subpixel_antialias"
	],
	"font_size": 12.5,
	"ignored_packages":
	[
		"Markdown",
		"Vintage"
	],
	"indent_guide_options":
	[
		"draw_normal",
		"draw_active"
	],
	"overlay_scroll_bars": "enabled",
	"save_on_focus_lost": true,
	"theme": "Material-Theme-Darker.sublime-theme",
	"translate_tabs_to_spaces": true,
	"material_theme_accent_yellow": true,
	"material_theme_bright_scrollbars": true,
	"material_theme_compact_panel": true,
	"material_theme_contrast_mode": false,
	"material_theme_panel_separator": true,
}

```

1. side bar 美化
    - boxy theme
        "theme": "Boxy Tomorrow.sublime-theme",
    - a file icon
2. 成对符号标示
    - BracketHighLighter
3. python 注释
    - DocBlockr Python
        "formatter": "google"
4. 文件自动添加头部信息
    - file header
        - python.tmpl
        
        ```
          # @ {{file_name}}
          # @Author: {{author}}
          # @Date:   {{create_time}}
          # @Last Modified by:   {{last_modified_by}}
          # @Last Modified time: {{last_modified_time}}
        ```
5. HTML快速生成
    - emmet
6. python 文档提示
    - anaconda
    
    ```
    {
        "complete_parameters": false,
        "pep8_max_line_length": 119,
        "anaconda_linter_mark_style": "squiggly_underline",
        "autoformat_ignore":
        [
            "E309",
            "E221"
        ],
        "pep8_ignore":
        [
            "E309",
            "E221"
        ],
    }
    ```
7. Python pep8
    - python PEP8 autoformat
    
     ```
      {
          "autoformat_on_save": false,
          "max-line-length": 119,
      }
     ```
8. 格式美化
    - HTML/CSS/JS prettify
    - JsFormat
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNTQ1MjI3MjVdfQ==
-->