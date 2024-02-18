# viz.py
#    
# Show a wordcloud for a precribed range of Scripture
#
# Copyright (c) 2022-2024 WordTM Project 
# Author: Johnny Cheng <drjohnnycheng@gmail.com>
#
# Updated: 28 January 2024
#
# URL: https://github.com/drjohnnycheng/wordtm.git
# For license information, see LICENSE.TXT

import numpy as np
import pandas as pd
from importlib_resources import files
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image

from wordtm import util


def plot_cloud(wordcloud):
    """Plot the prepared 'wordcloud'
    :param wordcloud: The WordCloud object for plotting, default to None
    :type wordcloud: WordCloud object
    """

    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloud) 
    plt.axis("off");


def show_wordcloud(docs, image='heart.jpg'):
    """Prepare and show a wordcloud

    :param docs: The collection of documents for preparing a wordcloud,
        default to None
    :type docs: pandas.DataFrame
    :param image: The filename of the image as the mask of the wordcloud,
        default to 'heart.jpg'
    :type image: str, optional
    """

    if image:
        img_file = files('wordtm.images').joinpath(image)
        mask = np.array(Image.open(img_file))
    else:
        mask = None

    if isinstance(docs, pd.DataFrame):
        docs = ' '.join(list(docs.text))
    elif isintance(docs, list) or isinstance(docs, np.ndarray):
        docs = ' ' .join(docs)

    wordcloud = WordCloud(background_color='black', colormap='Set2', mask=mask) \
                    .generate(docs)

    plot_cloud(wordcloud)


def chi_wordcloud(docs, image='heart.jpg'):
    """Prepare and show a Chinese wordcloud

    :param docs: The collection of Chinese documents for preparing a wordcloud,
        default to None
    :type docs: pandas.DataFrame
    :param image: The filename of the image as the mask of the wordcloud,
        default to 'heart.jpg'
    :type image: str, optional
    """

    util.set_lang('chi')
    diction = util.get_diction(docs)

    if image:
        img_file = files('wordtm.images').joinpath(image)
        mask = np.array(Image.open(img_file))
    else:
        mask = None

    font = 'msyh.ttc'
    wordcloud = WordCloud(background_color='black', colormap='Set2', 
                          mask=mask, font_path=font) \
                    .generate_from_frequencies(frequencies=diction)

    plot_cloud(wordcloud)
