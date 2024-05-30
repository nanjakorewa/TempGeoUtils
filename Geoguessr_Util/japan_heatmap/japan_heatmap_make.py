import os
import sys
import pandas as pd
from japanmap import picture
import matplotlib.pyplot as plt
import japanize_matplotlib as jam
import argparse

def map_draw(
    df,
    title="None"
):
    """csvのデータからヒートマップを作製する

    Args:
        df (pandas.DataFrame): ヒートマップを作成するcsvパス

    Returns:
        戻り値の型: 戻り値の説明 (例 : True なら成功, False なら失敗.)
    """
    cmap = plt.get_cmap('Reds')
    norm = plt.Normalize(vmin=df.value.min(), vmax=df.value.max())
    fcol = lambda x: '#' + bytes(cmap(norm(x), bytes=True)[:3]).hex()
    
    fig, ax = plt.subplots()
    jam.japanize()
        
    plt.colorbar(
        plt.cm.ScalarMappable(
            norm,
            cmap,
            # cax=ax.inset_axes([0.95, 0.1, 0.05, 0.8])
        ),
        ax=plt.gca()
    )

    plt.imshow(picture(df['value'].apply(fcol)))
    plt.title(title)
    return fig