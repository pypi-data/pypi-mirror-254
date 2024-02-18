from setuptools import find_packages, setup

setup(
    name='caad-rpa',  # パッケージ名(プロジェクト名)
    packages=find_packages(),  # パッケージ内(プロジェクト内)のパッケージ名をリスト形式で指定
    version='1.0.0',  # バージョン
    author='odxチーム',  # パッケージ作者の名前
    author_email='caad_odx_team@ca-adv.co.jp',  # パッケージ作者の連絡先メールアドレス
    description='RPAライブラリ',  # パッケージの簡単な説明
    long_description_content_type='text/markdown',
    # long_descriptionの形式を'text/plain', 'text/x-rst', 'text/markdown'のいずれかから指定
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
