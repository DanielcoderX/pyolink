# Pyolink

![Python](https://img.shields.io/badge/python-3.6%2B-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Jinja](https://img.shields.io/badge/jinja-%23FFFFFF.svg?style=for-the-badge&logo=jinja&logoColor=black)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

Pyolink is a front page generator from GitHub repositories.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required dependencies for Pyolink.

```bash
pip install -r requirements.txt
```

## Usage

To generate a front page for your GitHub repositories, run the following command:

```bash
python pyolink.py --username <GitHub username> --theme <theme name>
```

- The `--username` option specifies your GitHub username. If not provided, it defaults to "DanielcoderX".
- The `--theme` option specifies the theme to use for the front page. Currently, only the "first" theme is available. If not provided, it defaults to the "first" theme.

The generated front page will showcase your GitHub repositories in a visually appealing manner.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## TODO

- Add more themes to enhance the customization options.
- After adding a new theme, modify the `src/themes.yaml` file to include the new theme.

Feel free to explore the different themes and customize your front page to suit your personal style and preferences.