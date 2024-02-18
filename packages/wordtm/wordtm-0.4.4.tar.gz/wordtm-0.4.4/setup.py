from setuptools import setup, find_packages

VERSION = '0.4.4' 
DESCRIPTION = 'Topic Modeling Package'
LONG_DESCRIPTION = 'An NLP package for topic modeling on the Holy Scripture from low-code to pro-code'

# Setting up
setup(
        name="wordtm", 
        version=VERSION,
        author="Dr. Johnny CHENG",
        author_email="<drjohnnycheng@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        project_urls={
            'Documentation': 'https://drjohnnycheng.github.io/wordtm',
        },
        include_package_data=True,
        packages=find_packages(),
        package_data={
            'wordtm': ['wordtm/data/*.csv', 'wordtm/data/*.txt', 'wordtm/dictionary/*.txt',
            'wordtm/images/*.jpg', 'docs/*.html', 'docs/*.css'],
        },
        install_requires=['numpy', 'pandas', 'importlib_resources', 'regex', 'nltk', \
                    'matplotlib', 'wordcloud', 'pillow', 'jieba', 'gensim', 'pyLDAvis',  \
                    'bertopic',  'transformers', 'spacy', 'seaborn', \
                    'importlib', 'networkx', 'plotly', 'IPython', 'scikit-learn', 'torch'],
        
        keywords=['word', 'scripture', 'topic modeling', 'visualization', \
                  'low-code', 'pro-code', 'network analysis', 'BERTopic', \
                  'LDA', 'NFM'],

        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "Intended Audience :: Religion",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: MacOS :: MacOS X",
        ]
)
