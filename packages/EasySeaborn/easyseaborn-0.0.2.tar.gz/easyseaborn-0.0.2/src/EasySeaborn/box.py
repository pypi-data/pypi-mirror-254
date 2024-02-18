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
    >>> import sys
    >>> sys.path.append(r"D:\document\statistics\TidyStatsProject")
    >>> from EasySeaborn import box
    >>> import matplotlib.pyplot as plt
    >>> from SoEasyData import GetSeabornData
    >>> import numpy as np
    >>> titanic = GetSeabornData("titanic")
    >>> flights = GetSeabornData("flights")
    ===============================================================================1
    测试df参数(绘制整个dataframe中数值变量的估计量和误差值)
    >>> ax = box(titanic, savefilename="./image/box1.png",block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================2
    测试df参数(某列箱线图)
    >>> ax = box(titanic["age"], savefilename="./image/box2.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================3
    测试xvarname参数(给定x轴数值变量，单个变量绘制水平箱线图)
    >>> ax = box(titanic, xvarname="age", savefilename="./image/box3.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================4
    测试yvarname参数(给定y轴数值变量，单个变量绘制竖直箱线图)
    >>> ax = box(titanic, yvarname="age", savefilename="./image/box4.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================5
    测试xvarname和yvarname参数(给定xy轴变量，一个字符一个数值，竖直分组箱线图)
    >>> ax = box(titanic, xvarname="sex", yvarname="age", savefilename="./image/box5.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================6
    测试xvarname和yvarname参数(给定xy轴变量，两个数值，竖直分组箱线图)
    >>> ax = box(titanic, xvarname="survived", yvarname="age", savefilename="./image/box6.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================7
    测试groupby参数(给定XY变量下分组箱线图，颜色区分)
    >>> ax = box(titanic, xvarname="class", yvarname="age", groupby="class", savefilename="./image/box7.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================8
    测试groupby参数(给定XY变量下分组箱线图，类别区分)
    >>> ax = box(titanic, xvarname="class", yvarname="age", groupby="alive", savefilename="./image/box8.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================9
    测试一般绘图的标签参数
    >>> ax = box(titanic, xvarname="class", yvarname="age", groupby="alive", xlabel="X轴", ylabel="Y轴", title="标题", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, savefilename="./image/box9.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================10
    测试colormap参数(分组箱线图指定颜色映射)
    >>> ax = box(titanic, xvarname="class", yvarname="age", groupby="alive", colormap="Set2", savefilename="./image/box10.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================11
    测试colormap参数(分组箱线图指定颜色名称)
    >>> ax = box(titanic, xvarname="class", yvarname="age", groupby="alive", colormap=["red", "green"], savefilename="./image/box11.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================12
    测试fig_length和fig_width参数(图形大小)
    >>> ax = box(titanic, xvarname="class", yvarname="age", groupby="alive", fig_length=6, fig_width=8, savefilename="./image/box12.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================13
    测试layout参数(画布布局)
    >>> ax = box(titanic, xvarname="class", yvarname="age", groupby="alive", layout="constrained", savefilename="./image/box13.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", groupby="alive", layout="compressed", savefilename="./image/box14.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", groupby="alive", layout="tight", savefilename="./image/box15.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", groupby="alive", layout=None, savefilename="./image/box16.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================14
    测试hue_order参数(分组变量中的顺序)
    >>> ax = box(titanic, xvarname="class", yvarname="age", groupby="alive", hue_order=["no", "yes"], savefilename="./image/box17.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", groupby="alive", hue_order=["yes", "no"], savefilename="./image/box18.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================15
    测试order参数(箱子在X轴或者Y轴的排列顺序)
    >>> ax = box(titanic, xvarname="class", yvarname="age", groupby="alive", order=["First", "Third", "Second"], savefilename="./image/box19.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", groupby="alive", order=["Third", "First", "Second"], savefilename="./image/box20.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", groupby="alive", order=["Third", "Second", "First"], savefilename="./image/box21.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================16
    测试fontfamily参数(指定字体样式)
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="X轴", ylabel="Y轴", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="方正舒体", savefilename="./image/box22.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="X轴", ylabel="Y轴", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="方正姚体", savefilename="./image/box23.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="X轴", ylabel="Y轴", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="仿宋", savefilename="./image/box24.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="X轴", ylabel="Y轴", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="黑体", savefilename="./image/box25.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="X轴", ylabel="Y轴", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="华文彩云", savefilename="./image/box26.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="X轴", ylabel="Y轴", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="华文仿宋", savefilename="./image/box27.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="X轴", ylabel="Y轴", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="华文琥珀", savefilename="./image/box28.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="X轴", ylabel="Y轴", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="华文楷体", savefilename="./image/box29.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="X轴", ylabel="Y轴", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="华文隶书", savefilename="./image/box30.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="X轴", ylabel="Y轴", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="华文宋体", savefilename="./image/box31.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="X轴", ylabel="Y轴", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="华文细黑", savefilename="./image/box32.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="X轴", ylabel="Y轴", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="华文新魏", savefilename="./image/box33.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="X轴", ylabel="Y轴", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="华文行楷", savefilename="./image/box34.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="X轴", ylabel="Y轴", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="华文中宋", savefilename="./image/box35.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="X轴", ylabel="Y轴", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="楷体", savefilename="./image/box36.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="X轴", ylabel="Y轴", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="隶书", savefilename="./image/box37.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="X轴", ylabel="Y轴", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="宋体", savefilename="./image/box38.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="X轴", ylabel="Y轴", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="新宋体", savefilename="./image/box39.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="X轴", ylabel="Y轴", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", savefilename="./image/box40.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="class", ylabel="age", title="box Plot", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="TimesNewRoman", savefilename="./image/box41.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", xlabel="class", ylabel="age", title="box Plot", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="Arial", savefilename="./image/box42.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================17
    测试isshowplot参数(是否显示图形)
    >>> ax = box(titanic, xvarname="class", yvarname="age", isshowplot=1, savefilename="./image/box43.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", isshowplot=0, savefilename="./image/box44.png", block=False)
    ===============================================================================18
    测试snsstyle参数(使用seaborn的风格)
    >>> ax = box(titanic, xvarname="class", yvarname="age", snsstyle="darkgrid", savefilename="./image/box45.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", snsstyle="whitegrid", savefilename="./image/box46.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", snsstyle="dark", savefilename="./image/box47.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", snsstyle="white", savefilename="./image/box48.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", snsstyle="ticks", savefilename="./image/box49.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================19
    测试isremoveleftspine参数(移除左轴线，snsstyle为ticks或者white时才有用)
    >>> ax = box(titanic, xvarname="class", yvarname="age", snsstyle="white", removeleftspine=1, savefilename="./image/box50.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", snsstyle="ticks", removeleftspine=0, savefilename="./image/box51.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================20
    测试isremoverightspine参数(移除右轴线，snsstyle为ticks或者white时才有用)
    >>> ax = box(titanic, xvarname="class", yvarname="age", snsstyle="white", removerightspine=1, savefilename="./image/box52.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", snsstyle="ticks", removerightspine=0, savefilename="./image/box53.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================21
    测试isremovetopspine参数(移除上轴线，snsstyle为ticks或者white时才有用)
    >>> ax = box(titanic, xvarname="class", yvarname="age", snsstyle="white", removetopspine=1, savefilename="./image/box54.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", snsstyle="ticks", removetopspine=0, savefilename="./image/box55.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================22
    测试isremovebottomspine参数(移除下轴线，snsstyle为ticks或者white时才有用)
    >>> ax = box(titanic, xvarname="class", yvarname="age", snsstyle="white", removebottomspine=1, savefilename="./image/box56.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", snsstyle="ticks", removebottomspine=0, savefilename="./image/box57.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================23
    测试offset参数(图形与轴线距离)
    >>> ax = box(titanic, xvarname="class", yvarname="age", snsstyle="ticks", offset=3, savefilename="./image/box58.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", offset=3, savefilename="./image/box59.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================24
    测试trim参数(设置R风格轴线)
    >>> ax = box(titanic, xvarname="class", yvarname="age", snsstyle="ticks", trim=1, savefilename="./image/box60.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", trim=1, savefilename="./image/box61.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================25
    测试contextstyle参数(绘图风格)
    >>> ax = box(titanic, xvarname="class", yvarname="age", contextstyle="notebook", savefilename="./image/box62.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", contextstyle="paper", savefilename="./image/box63.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", contextstyle="talk", savefilename="./image/box64.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", contextstyle="poster", savefilename="./image/box65.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================26
    测试matplotlibstyle参数(matplotlib支持的绘图风格)
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="Solarize_Light2", savefilename="./image/box66.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="_classic_test_patch", savefilename="./image/box67.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="_mpl-gallery", savefilename="./image/box68.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="_mpl-gallery-nogrid", savefilename="./image/box69.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="bmh", savefilename="./image/box70.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="classic", savefilename="./image/box71.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="dark_background", savefilename="./image/box72.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="fast", savefilename="./image/box73.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="fivethirtyeight", savefilename="./image/box74.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="ggplot", savefilename="./image/box75.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="grayscale", savefilename="./image/box76.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="seaborn-v0_8", savefilename="./image/box77.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="seaborn-v0_8-bright", savefilename="./image/box78.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="seaborn-v0_8-colorblind", savefilename="./image/box79.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="seaborn-v0_8-dark", savefilename="./image/box80.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="seaborn-v0_8-dark-palette", savefilename="./image/box81.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="seaborn-v0_8-darkgrid", savefilename="./image/box82.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="seaborn-v0_8-deep", savefilename="./image/box83.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="seaborn-v0_8-muted", savefilename="./image/box84.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="seaborn-v0_8-notebook", savefilename="./image/box85.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="seaborn-v0_8-paper", savefilename="./image/box86.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="seaborn-v0_8-pastel", savefilename="./image/box87.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="seaborn-v0_8-poster", savefilename="./image/box88.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="seaborn-v0_8-talk", savefilename="./image/box89.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="seaborn-v0_8-ticks", savefilename="./image/box90.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="seaborn-v0_8-white", savefilename="./image/box91.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="seaborn-v0_8-whitegrid", savefilename="./image/box92.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(flights, xvarname="month", yvarname="passengers", matplotlibstyle="tableau-colorblind10", savefilename="./image/box93.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================27
    测试boxparamsdict参数中orient参数(箱线图朝向)
    >>> ax = box(titanic, yvarname="survived", xvarname="age", boxparamsdict={"orient": "h"}, savefilename="./image/box94.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================28
    测试boxparamsdict参数中color参数(箱子颜色)
    >>> ax = box(titanic, xvarname="class", yvarname="age", boxparamsdict={"color": "green"}, savefilename="./image/box95.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================29
    测试boxparamsdict参数中isfill参数(不填充颜色)
    >>> ax = box(titanic, xvarname="class", yvarname="age", boxparamsdict={"isfill": 0}, savefilename="./image/box96.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================30
    测试boxparamsdict参数中saturation参数(颜色饱和度)
    >>> ax = box(titanic, xvarname="class", yvarname="age", boxparamsdict={"saturation": 0.3}, savefilename="./image/box97.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================31
    测试boxparamsdict参数中dodge参数(分组排列方式)
    >>> ax = box(titanic, xvarname="class", yvarname="age", groupby="sex", boxparamsdict={"dodge": 1}, savefilename="./image/box98.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="class", yvarname="age", groupby="sex", boxparamsdict={"dodge": 0}, savefilename="./image/box99.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================32
    测试boxparamsdict参数中gap参数(增加分组之间的间距)
    >>> ax = box(titanic, xvarname="class", yvarname="age", groupby="alive", boxparamsdict={"gap": 0.2}, savefilename="./image/box100.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================33
    测试boxparamsdict参数中whis参数(异常值范围)
    >>> ax = box(titanic, xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"whis": (0, 100)}, savefilename="./image/box101.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"whis": 2}, savefilename="./image/box102.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================34
    测试boxparamsdict参数中width参数(箱子宽度)
    >>> ax = box(titanic, xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"width": 0.4}, savefilename="./image/box103.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================35
    测试boxparamsdict参数中linecolor,linewidth参数(箱子样式)
    >>> ax = box(titanic, xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"color": "0.8", "linecolor": "#137", "linewidth": 0.75}, savefilename="./image/box104.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================36
    测试boxparamsdict参数中fliersize参数(异常值点大小)
    >>> ax = box(titanic, xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"fliersize": 1}, savefilename="./image/box105.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================37
    测试boxparamsdict参数中legend参数(指定图例样式)
    >>> ax = box(titanic, xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"saturation": 0.2, "legend": "auto"}, savefilename="./image/box106.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"saturation": 0.4, "legend": "full"}, savefilename="./image/box107.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"saturation": 0.7, "legend": "brief"}, savefilename="./image/box108.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = box(titanic, xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"saturation": 0.9, "legend": False}, savefilename="./image/box109.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================38
    测试boxparamsdict参数中isnotch参数(设置有缺口的箱线图)
    >>> ax = box(titanic, xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"saturation": 0.1, "isnotch": 1}, savefilename="./image/box110.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================39
    测试boxparamsdict参数中isshowmean参数(显示均值线)
    >>> ax = box(titanic, xvarname="deck", yvarname="age", boxparamsdict={"isshowmean": 1, "meanlinecolor": "green", "meanlinewidth": 1.2}, savefilename="./image/box111.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================40
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
