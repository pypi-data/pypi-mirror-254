import matplotlib.pyplot as plt
from matplotlib import font_manager
from pathlib import Path
import seaborn as sns
import warnings
# 禁用警告
warnings.filterwarnings("ignore")

# 获取包所在的路径
current_PACKAGE_PATH = Path(__file__).resolve().parent


def fit(
        df=None,
        xvarname=None,
        yvarname=None,
        groupby=None,
        xlabel=None,
        ylabel=None,
        title=None,
        xlabelsize=12,
        ylabelsize=12,
        titlesize=12,
        xticklabelsize=12,
        yticklabelsize=12,
        xticklabelrotation=0,
        yticklabelrotation=0,
        colormap=None,
        alpha=None,
        fig_length=6.4,
        fig_width=4.8,
        layout="tight",
        hue_order=None,
        order=None,
        fontfamily="华文楷体",
        isshowplot=1,
        savefilename=None,
        snsstyle="darkgrid",
        removeleftspine=0,
        removerightspine=1,
        removetopspine=1,
        removebottomspine=0,
        offset=None,
        trim=0,
        contextstyle="notebook",
        matplotlibstyle=None,
        fitparamsdict={
            "col": None,
            "row": None,
            "marker": 'o',
            "col_order": None,
            "row_order": None,
            "islegend": 1,
            "isscatter": 1,
            "isreg": 1,
            "ci": 95,
            "order": 1,
            "islogistic": 0,
            "islowess": 0,
            "isrobust": 0,
            "issharex": 1,
            "issharey": 1,
            "islegendout": 1,
            "subplot_kws": None,
            "title": None},
        **kwargs):
    """
    这是一个Seaborn绘制回归拟合图函数的文档字符串。

    参数:
    df (pd.DataFrame object): dataframe。
    xvarname (str): X轴变量名。
    yvarname (str): Y轴变量名。
    groupby (str): 分组变量名。
    xlabel (str): X轴标签。
    ylabel (str): Y轴标签。
    title (str): 图形标题。
    xlabelsize (numeric): X轴标签字体大小。
    ylabelsize (numeric): Y轴标签字体大小。
    titlesize (numeric): 图形标题字体大小。
    xticklabelsize (numeric): X轴刻度标签字体大小。
    yticklabelsize (numeric): Y轴刻度标签字体大小。
    xticklabelrotation (numeric): X轴刻度标签旋转角度。
    yticklabelrotation (numeric): Y轴刻度标签旋转角度。
    colormap (str): 颜色映射名称。
    alpha (numeric): 颜色透明度。
    fig_length (numeric): 图形长度。
    fig_width (numeric): 图形宽度。
    layout (str ; None): 图形在画布上的布局机制{"constrained", "compressed", "tight", None}。
    hue_order (list or array-like): 分组变量的顺序。
    order (list or array-like): 图形主体的顺序。
    fontfamily (str): 支持的中英文字体名称{"方正舒体", "方正姚体", "仿宋", "黑体", "华文彩云", "华文仿宋", "华文琥珀", "华文楷体", "华文隶书", "华文宋体", "华文细黑", "华文新魏", "华文行楷", "华文中宋", "楷体", "隶书", "宋体", "微软雅黑", "新宋体", "幼圆", "TimesNewRoman", "Arial"}。
    isshowplot (binary): 是否显示图形{1,0}。
    savefilename (str): 保存的图形文件名（带后缀）{".pdf", ".png", ".jpg"}。
    snsstyle (str): seaborn绘图风格样式{"darkgrid", "whitegrid", "dark", "white", "ticks"}。
    isremoveleftspine (binary): 是否移除左轴线{1,0}。
    isremoverightspine (binary): 是否移除右轴线{1,0}。
    isremovetopspine (binary): 是否移除上轴线{1,0}。
    isremovebottomspine (binary): 是否移除下轴线{1,0}。
    offset (numeric): 轴线距离图形的距离。
    trim (binary): 是否设置R风格轴线{1,0}。
    contextstyle (str): 图形元素大小风格调整{"paper", "notebook", "talk", "poster"}。
    matplotlibstyle (str): matplotlib支持的绘图风格{"Solarize_Light2", "_classic_test_patch", "_mpl-gallery", "_mpl-gallery-nogrid", "bmh", "classic", "dark_background", "fast", "fivethirtyeight", "ggplot", "grayscale", "seaborn-v0_8", "seaborn-v0_8-bright", "seaborn-v0_8-colorblind", "seaborn-v0_8-dark", "seaborn-v0_8-dark-palette", "seaborn-v0_8-darkgrid", "seaborn-v0_8-deep", "seaborn-v0_8-muted", "seaborn-v0_8-notebook", "seaborn-v0_8-paper", "seaborn-v0_8-pastel", "seaborn-v0_8-poster", "seaborn-v0_8-talk", "seaborn-v0_8-ticks", "seaborn-v0_8-white", "seaborn-v0_8-whitegrid", "tableau-colorblind10"}。
    fitparamsdict (dict): 控制函数拟合图的参数。
    {
        col (str): 列分组变量。
        row (str): 行分组变量。
        marker (str): 散点样式。
        col_order (list of str): 列分组变量的顺序。
        row_order (list of str): 行分组变量的顺序。
        islegend (binary): 是否显示图例{1,0}。
        isscatter (binary): 是否绘制散点{1,0}。
        isreg (binary): 是否绘制回归拟合曲线{1,0}。
        ci (numeric or None): 置信度[0,100]。
        order (numeric): 多项式回归的阶数。
        islogistic (binary): 是否拟合逻辑回归{1,0}。
        islowess (binary): 是否拟合局部多项式回归{1,0}。
        isrobust (binary): 是否拟合稳健回归{1,0}。
        issharex (binary): 是否共享X轴坐标{1,0}。
        issharey (binary): 是否共享Y轴坐标{1,0}。
        islegendout (binary): 是否将图例放到图形外面{1,0}。
        subplot_kws (dict): 控制子图的相关参数字典。
        {
            (xy)label_(i) (str): 从左到右从上到下第i个子图的xy轴标签。
            title_(i) (str): 从左到右从上到下第i个子图的图形标题。
            (xy)labelsize_(i) (numeric): 从左到右从上到下第i个子图的xy轴标签字体大小。
            titlesize (numeric): 从左到右从上到下第i个子图的图形标题字体大小。
            (xy)ticklabelsize_(i) (numeric): 从左到右从上到下第i个子图的xy轴刻度标签字体大小。
            (xy)ticklabelrotation_i (numeric): 从左到右从上到下第i个子图的xy轴刻度标签旋转角度。
        }
        title (str): 图形标题。
    }

    返回值：
    Axes对象或者是Axes构成的二维数组

    示例：
    ===============================================================================0
    导入模块
    >>> from TidySeaborn import TidySeabornFlexible
    >>> import matplotlib.pyplot as plt
    >>> from TidySeaborn import GetSeabornData
    >>> import numpy as np
    >>> iris = GetSeabornData("iris")
    >>> tips = GetSeabornData("tips")
    >>> penguins = GetSeabornData("penguins")
    >>> planets = GetSeabornData("planets")
    >>> flights = GetSeabornData("flights")
    >>> titanic = GetSeabornData("titanic")
    >>> diamonds = GetSeabornData("diamonds")
    >>> geyser = GetSeabornData("geyser")
    >>> fmri = GetSeabornData("fmri")
    >>> mpg = GetSeabornData("mpg")
    >>> glue = GetSeabornData("glue")
    测试函数拟合图
    ===============================================================================129
    单个函数拟合
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================130
    分组函数拟合
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================131
    指定列分组
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", fitparamsdict={"col": "sex"}, fig_width=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================132
    指定列分组和行分组
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species"}, fig_width=3, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================133
    不共享xy轴坐标
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "issharex": 0, "issharey": 0}, fig_width=3, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================134
    散点样式
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "marker": "^"}, fig_width=2.5, fig_length=3, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================135
    列分组变量的顺序
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "col_order": ["Chinstrap", "Gentoo", "Adelie"]}, fig_width=2.5, fig_length=3, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================136
    行分组变量的顺序
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "col_order": ["Chinstrap", "Gentoo", "Adelie"], "row_order": ["Female", "Male"]}, fig_width=2.5, fig_length=3, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================137
    不显示图例
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "islegend": 0}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================138
    不绘制散点
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "islegend": 0, "isscatter": 0}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================139
    不绘制拟合回归线
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "isreg": 0}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================140
    指定置信区间的置信度
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "ci": 90}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================141
    多项式回归
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "order": 2}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================142
    局部多项式回归
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "islowess": 1}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================143
    稳健回归
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "isrobust": 1}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================144
    图例设置到图形外面
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"row": "species", "islegendout": 1}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"row": "species", "islegendout": 0}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================145
    子图控制
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================146
    总标题
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "title": "总标题"}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================147
    测试一般绘图的字体参数
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================148
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", savefilename="./image/函数拟合图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================149
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================150
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================151
    """
    # 字体对应
    fontfamily_dic = {
        "方正舒体": "FZSTK.TTF",
        "方正姚体": "FZYTK.TTF",
        "仿宋": "simfang.ttf",
        "黑体": "simhei.ttf",
        "华文彩云": "STCAIYUN.TTF",
        "华文仿宋": "STFANGSO.TTF",
        "华文琥珀": "STHUPO.TTF",
        "华文楷体": "STKAITI.TTF",
        "华文隶书": "STLITI.TTF",
        "华文宋体": "STSONG.TTF",
        "华文细黑": "STXIHEI.TTF",
        "华文新魏": "STXINWEI.TTF",
        "华文行楷": "STXINGKA.TTF",
        "华文中宋": "STZHONGS.TTF",
        "楷体": "simkai.ttf",
        "隶书": "SIMLI.TTF",
        "宋体": "simsun.ttc",
        "微软雅黑": "msyhl.ttc",
        "新宋体": "simsun.ttc",
        "幼圆": "SIMYOU.TTF",
        "TimesNewRoman": "times.ttf",
        "Arial": "arial.ttf"
    }
    # 设置字体路径
    fontpath = Path(
        current_PACKAGE_PATH, "fonts/{}".format(fontfamily_dic[fontfamily]))
    fontobj = font_manager.FontProperties(fname=fontpath)
    # 默认的字典
    fitparamsdictdefault = {
        "col": None,
        "row": None,
        "marker": 'o',
        "col_order": None,
        "row_order": None,
        "islegend": 1,
        "isscatter": 1,
        "isreg": 1,
        "ci": 95,
        "order": 1,
        "islogistic": 0,
        "islowess": 0,
        "isrobust": 0,
        "issharex": 1,
        "issharey": 1,
        "islegendout": 1,
        "subplot_kws": None,
        "title": None}
    # 更新字典
    fitparamsdictdefault.update(fitparamsdict)
    if matplotlibstyle is None:
        with sns.axes_style(snsstyle):
            sns.set_context(contextstyle)
            # 核心变量参数，颜色参数，图形参数
            facet = sns.lmplot(
                data=df,
                x=xvarname,
                y=yvarname,
                hue=groupby,
                palette=colormap,
                hue_order=hue_order,
                height=fig_width if fig_width == 5 else 5,
                aspect=fig_length / fig_width if fig_length / fig_width == 1 else 1,
                col=fitparamsdictdefault["col"],
                row=fitparamsdictdefault["row"],
                col_order=fitparamsdictdefault["col_order"],
                row_order=fitparamsdictdefault["row_order"],
                markers=fitparamsdictdefault["marker"],
                legend=bool(
                    fitparamsdictdefault["islegend"]),
                scatter=bool(
                    fitparamsdictdefault["isscatter"]),
                fit_reg=bool(
                    fitparamsdictdefault["isreg"]),
                ci=fitparamsdictdefault["ci"],
                order=fitparamsdictdefault["order"],
                logistic=bool(
                    fitparamsdictdefault["islogistic"]),
                lowess=bool(
                    fitparamsdictdefault["islowess"]),
                robust=bool(
                    fitparamsdictdefault["isrobust"]),
                facet_kws={
                    "sharex": bool(
                        fitparamsdictdefault["issharex"]),
                    "sharey": bool(
                        fitparamsdictdefault["issharey"]),
                    "legend_out": bool(
                        fitparamsdictdefault["islegendout"])})
    else:
        with plt.style.context(matplotlibstyle):
            # 核心变量参数，颜色参数，图形参数
            facet = sns.lmplot(
                data=df,
                x=xvarname,
                y=yvarname,
                hue=groupby,
                palette=colormap,
                hue_order=hue_order,
                height=fig_width if fig_width == 5 else 5,
                aspect=fig_length / fig_width if fig_length / fig_width == 1 else 1,
                col=fitparamsdictdefault["col"],
                row=fitparamsdictdefault["row"],
                col_order=fitparamsdictdefault["col_order"],
                row_order=fitparamsdictdefault["row_order"],
                markers=fitparamsdictdefault["marker"],
                legend=bool(
                    fitparamsdictdefault["islegend"]),
                scatter=bool(
                    fitparamsdictdefault["isscatter"]),
                fit_reg=bool(
                    fitparamsdictdefault["isreg"]),
                ci=fitparamsdictdefault["ci"],
                order=fitparamsdictdefault["order"],
                logistic=bool(
                    fitparamsdictdefault["islogistic"]),
                lowess=bool(
                    fitparamsdictdefault["islowess"]),
                robust=bool(
                    fitparamsdictdefault["isrobust"]),
                facet_kws={
                    "sharex": bool(
                        fitparamsdictdefault["issharex"]),
                    "sharey": bool(
                        fitparamsdictdefault["issharey"]),
                    "legend_out": bool(
                        fitparamsdictdefault["islegendout"])})
    fig = facet.fig
    axes = facet.axes
    axes = axes.flatten()
    subplotkws = fitparamsdictdefault["subplot_kws"]
    if subplotkws is not None:
        for ax, i in zip(axes, range(1, len(axes) + 1)):
            # 标题参数
            if subplotkws.get("xlabel_{}".format(i), None) is not None:
                ax.set_xlabel(subplotkws["xlabel_{}".format(i)], fontproperties=fontobj,
                                fontsize=subplotkws.get("xlabelsize_{}".format(i), 12))
            if subplotkws.get("ylabel_{}".format(i), None) is not None:
                ax.set_ylabel(subplotkws["ylabel_{}".format(i)], fontproperties=fontobj,
                                fontsize=subplotkws.get("ylabelsize_{}".format(i), 12))
            if subplotkws.get("title_{}".format(i), None) is not None:
                ax.set_title(subplotkws["title_{}".format(
                    i)], fontproperties=fontobj, fontsize=subplotkws.get("titlesize", 12))
            # 刻度参数，刻度标签参数
            ax.tick_params(
                'x', labelsize=subplotkws.get(
                    "xticklabelsize_{}".format(i), 12), rotation=subplotkws.get(
                    "xticklabelrotation_{}".format(i), 0))
            ax.tick_params(
                'y', labelsize=subplotkws.get(
                    "yticklabelsize_{}".format(i), 12), rotation=subplotkws.get(
                    "yticklabelrotation_{}".format(i), 0))
            ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(),
                            fontproperties=fontobj)
            ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(),
                            fontproperties=fontobj)
    else:
        pass
    # 移除spines
    sns.despine(
        left=removeleftspine,
        right=removerightspine,
        top=removetopspine,
        bottom=removebottomspine,
        offset=offset,
        trim=trim)
    if fitparamsdictdefault["title"] is not None:
        plt.suptitle(fitparamsdictdefault["title"], fontproperties=fontobj)
    else:
        pass
    if savefilename is not None:
        fig.savefig(savefilename)
    else:
        pass
    if bool(isshowplot):
        plt.show(**kwargs)
    else:
        pass
    return axes
    