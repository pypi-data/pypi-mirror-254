import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name="open-meteo-weather-sample-jpcity", # PEP503, PEP508に従いハイフン
    version="0.0.dev2", # PEP440に従った体系。ここでは「Development release」と位置付ける
    install_requires = requirements,  # requirements.txt の内容をそのままコピー
    entry_points={
        'console_scripts': [
            'open_meteo_weather_sample_jpcity=open_meteo_weather_sample_jpcity:main',
            # PEP8に従いアンダースコア
        ],
    },
    packages=setuptools.find_packages(), # 直下のパッケージ仕様のフォルダ名をリスト形式で全て取得
    description="sample distribution-packages by legacy-setup.py",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Hoshimado"
    # author_email="sample@example.com",
    # python_requires='>=3.7',
)
