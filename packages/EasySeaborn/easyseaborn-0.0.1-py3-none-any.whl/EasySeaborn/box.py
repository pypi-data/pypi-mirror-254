import matplotlib.pyplot as plt
from matplotlib import font_manager
from pathlib import Path
import seaborn as sns
import warnings
# 禁用警告
warnings.filterwarnings("ignore")

# 获取包所在的路径
current_PACKAGE_PATH = Path(__file__).resolve().parent


def box(
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
        boxparamsdict={
            "orient": None,
            "color": None,
            "saturation": 0.75,
            "isfill": 1,
            "dodge": "auto",
            "width": 0.8,
            "gap": 0,
            "whis": 1.5,
            "linecolor": "auto",
            "linewidth": None,
            "fliersize": None,
            "islog": 0,
            "legend": "auto",
            "isnotch": 0,
            "isshowmean": 0,
            "isshowfliers": 1,
            "meanlinecolor": "red",
            "meanlinewidth": 1},
        **kwargs):
    """
    这是一个Seaborn绘制箱线图函数的文档字符串。

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
    boxparamsdict (dict): 控制箱线图的参数字典
    {
        orient (str): 箱线图的方向{"v", "h"}。
        color (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 箱子的填充颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        saturation (float): 颜色透明度。
        isfill (binary): 是否填充颜色{1,0}。
        dodge (str or binary): 是否设置分组箱线图的排列方式为并排排列{"auto", 1, 0}。
        width (numeric): 箱子的宽度。
        gap (numeric): 分组箱线图的排列方式为并排排列时箱子之间的间隔。
        whis (numeric): 用于控制多少倍IQR以外作为异常值或者是正常值范围元组。
        linecolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 线条颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        linewidth (numeric): 线宽。
        fliersize (numeric): 异常值点的大小。
        islog (binary or positive numeric): 是否对数化(以10为底)后再绘制箱线图{1,0}或者是对数的底数。
        legend (str): 指定图例的样式{"auto", "brief", "full", False}。
        isnotch (binary): 是否绘制有缺口的箱线图{1,0}。
        isshowmean (binary): 是否显示均值线{1,0}。
        isshowfliers (binary): 是否显示异常值点{1,0}。
        meanlinecolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 均值线颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        meanlinewidth (numeric): 均值线条宽度。
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
    测试箱线图参数
    ===============================================================================62
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="age", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================63
    分组箱线图
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="age", yvarname="class", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================64
    二分组箱线图
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="age", yvarname="class", groupby="alive", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================65
    不填充颜色
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="class", yvarname="age", groupby="alive", boxparamsdict={"isfill": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================66
    增加分组之间的间距
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="class", yvarname="age", groupby="alive", boxparamsdict={"isfill": 0, "gap": 0.2}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================67
    分组排列方式
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="class", yvarname="age", groupby="alive", boxparamsdict={"isfill": 0, "gap": 0.2, "dodge": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="class", yvarname="age", groupby="alive", boxparamsdict={"isfill": 0, "gap": 0.2, "dodge": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================68
    异常值范围
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"whis": (0, 100)}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"whis": 2}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================69
    箱子宽度
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"width": 0.4}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================70
    箱子样式
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"color": "0.8", "linecolor": "#137", "linewidth": 0.75}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================71
    异常值点大小
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="fare", yvarname="age", groupby="alive", boxparamsdict={"fliersize": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================72
    颜色饱和度
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", boxparamsdict={"saturation": 0.2}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================73
    指定图例样式
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"saturation": 0.2, "legend": "auto"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"saturation": 0.4, "legend": "full"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"saturation": 0.7, "legend": "brief"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"saturation": 0.9, "legend": False}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================74
    设置有缺口的箱线图
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"saturation": 0.1, "isnotch": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================75
    显示均值线
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", boxparamsdict={"isshowmean": 1, "meanlinecolor": "green", "meanlinewidth": 1.2}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================76
    显示异常值点
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", boxparamsdict={"isshowfliers": 1, "whis": (0, 50)}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================77
    测试一般绘图的标签参数
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================78
    测试一般绘图的字体参数
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================79
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", savefilename="./image/箱线图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================80
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================81
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================82
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
    boxparamsdictdefault = {
        "orient": None,
        "color": None,
        "saturation": 0.75,
        "isfill": 1,
        "dodge": "auto",
        "width": 0.8,
        "gap": 0,
        "whis": 1.5,
        "linecolor": "auto",
        "linewidth": None,
        "fliersize": None,
        "islog": 0,
        "legend": "auto",
        "isnotch": 0,
        "isshowmean": 0,
        "isshowfliers": 1,
        "meanlinecolor": "red",
        "meanlinewidth": 1}
    # 更新字典
    boxparamsdictdefault.update(boxparamsdict)
    if matplotlibstyle is None:
        with sns.axes_style(snsstyle):
            sns.set_context(contextstyle)
            # 开始绘图，画布参数
            fig, ax = plt.subplots(
                figsize=(fig_length, fig_width), layout=layout)
            # 核心变量参数，颜色参数，图形参数
            sns.boxplot(
                data=df,
                x=xvarname,
                y=yvarname,
                hue=groupby,
                ax=ax,
                palette=colormap,
                hue_order=hue_order,
                order=order,
                orient=boxparamsdictdefault["orient"],
                color=boxparamsdictdefault["color"],
                saturation=boxparamsdictdefault["saturation"],
                fill=bool(
                    boxparamsdictdefault["isfill"]),
                dodge=boxparamsdictdefault["dodge"] if boxparamsdictdefault["dodge"] == "auto" else bool(
                    boxparamsdictdefault["dodge"]),
                width=boxparamsdictdefault["width"],
                gap=boxparamsdictdefault["gap"],
                whis=boxparamsdictdefault["whis"],
                linecolor=boxparamsdictdefault["linecolor"],
                linewidth=boxparamsdictdefault["linewidth"],
                fliersize=boxparamsdictdefault["fliersize"],
                log_scale=bool(
                    boxparamsdictdefault["islog"]) if boxparamsdictdefault["islog"] == 1 or boxparamsdictdefault["islog"] == 0 else boxparamsdictdefault["islog"],
                legend=boxparamsdictdefault["legend"],
                notch=bool(
                    boxparamsdictdefault["isnotch"]),
                showmeans=bool(
                    boxparamsdictdefault["isshowmean"]),
                meanline=bool(
                    boxparamsdictdefault["isshowmean"]),
                showfliers=bool(
                    boxparamsdictdefault["isshowfliers"]),
                meanprops={
                    "color": boxparamsdictdefault["meanlinecolor"],
                    "linewidth": boxparamsdictdefault["meanlinewidth"]})
    else:
        with plt.style.context(matplotlibstyle):
            # 开始绘图，画布参数
            fig, ax = plt.subplots(
                figsize=(fig_length, fig_width), layout=layout)
            # 核心变量参数，颜色参数，图形参数
            sns.boxplot(
                data=df,
                x=xvarname,
                y=yvarname,
                hue=groupby,
                ax=ax,
                palette=colormap,
                hue_order=hue_order,
                order=order,
                orient=boxparamsdictdefault["orient"],
                color=boxparamsdictdefault["color"],
                saturation=boxparamsdictdefault["saturation"],
                fill=bool(
                    boxparamsdictdefault["isfill"]),
                dodge=boxparamsdictdefault["dodge"] if boxparamsdictdefault["dodge"] == "auto" else bool(
                    boxparamsdictdefault["dodge"]),
                width=boxparamsdictdefault["width"],
                gap=boxparamsdictdefault["gap"],
                whis=boxparamsdictdefault["whis"],
                linecolor=boxparamsdictdefault["linecolor"],
                linewidth=boxparamsdictdefault["linewidth"],
                fliersize=boxparamsdictdefault["fliersize"],
                log_scale=bool(
                    boxparamsdictdefault["islog"]) if boxparamsdictdefault["islog"] == 1 or boxparamsdictdefault["islog"] == 0 else boxparamsdictdefault["islog"],
                legend=boxparamsdictdefault["legend"],
                notch=bool(
                    boxparamsdictdefault["isnotch"]),
                showmeans=bool(
                    boxparamsdictdefault["isshowmean"]),
                meanline=bool(
                    boxparamsdictdefault["isshowmean"]),
                showfliers=bool(
                    boxparamsdictdefault["isshowfliers"]),
                meanprops={
                    "color": boxparamsdictdefault["meanlinecolor"],
                    "linewidth": boxparamsdictdefault["meanlinewidth"]})
    # 标题参数
    if xlabel is not None:
        ax.set_xlabel(xlabel, fontproperties=fontobj,
                        fontsize=xlabelsize)
    if ylabel is not None:
        ax.set_ylabel(ylabel, fontproperties=fontobj,
                        fontsize=ylabelsize)
    if title is not None:
        ax.set_title(title, fontproperties=fontobj, fontsize=titlesize)
    # 刻度参数，刻度标签参数
    ax.tick_params('x', labelsize=xticklabelsize,
                    rotation=xticklabelrotation)
    ax.tick_params('y', labelsize=yticklabelsize,
                    rotation=yticklabelrotation)
    ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(),
                    fontproperties=fontobj)
    ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(),
                    fontproperties=fontobj)
    # 移除spines
    sns.despine(
        left=removeleftspine,
        right=removerightspine,
        top=removetopspine,
        bottom=removebottomspine,
        offset=offset,
        trim=trim)
    if savefilename is not None:
        fig.savefig(savefilename)
    else:
        pass
    if bool(isshowplot):
        plt.show(**kwargs)
    else:
        pass
    return ax
