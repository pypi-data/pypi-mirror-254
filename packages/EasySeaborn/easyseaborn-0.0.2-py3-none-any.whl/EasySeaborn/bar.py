import matplotlib.pyplot as plt
from matplotlib import font_manager
from pathlib import Path
import seaborn as sns
import warnings
# 禁用警告
warnings.filterwarnings("ignore")

# 获取包所在的路径
current_PACKAGE_PATH = Path(__file__).resolve().parent


def bar(
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
    barparamsdict={
            "estimator": "mean",
            "errorbar": (
                "ci",
                95),
            "n_boot": 1000,
            "seed": None,
            "orient": None,
            "color": None,
            "saturation": 0.75,
            "isfill": 1,
            "width": 0.8,
            "dodge": "auto",
            "gap": 0,
            "islog": 0,
            "legend": "auto",
            "capsize": 0,
            "isshowdatalabel": 0,
            "datalabelsize": 10,
            "datalabelformat": "%g",
            "datalabelcolor": "black",
            "errorbar_linewidth": 1,
            "errorbar_linecolor": "black",
            "errorbar_linestyle": "-"},
        **kwargs):
    """
    这是一个Seaborn绘制柱状误差图函数的文档字符串。

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
    colormap (str or list of str): 颜色映射名称或者颜色列表。
    fig_length (numeric): 图形长度。
    fig_width (numeric): 图形宽度。
    layout (str ; None): 图形在画布上的布局机制{"constrained", "compressed", "tight", None}。
    hue_order (list or array-like): 分组变量的顺序。
    order (list or array-like): 图形主体的顺序。
    fontfamily (str): 支持的中英文字体名称{"方正舒体", "方正姚体", "仿宋", "黑体", "华文彩云", "华文仿宋", "华文琥珀", "华文楷体", "华文隶书", "华文宋体", "华文细黑", "华文新魏", "华文行楷", "华文中宋", "楷体", "隶书", "宋体", "微软雅黑", "新宋体", "幼圆", "TimesNewRoman", "Arial"}。
    isshowplot (binary): 是否显示图形{1,0}。
    savefilename (str): 保存的图形文件名（带后缀）{".pdf", ".png", ".jpg"}。
    snsstyle (str): seaborn绘图风格样式{"darkgrid", "whitegrid", "dark", "white", "ticks"}。
    removeleftspine (binary): 是否移除左轴线{1,0}。
    removerightspine (binary): 是否移除右轴线{1,0}。
    removetopspine (binary): 是否移除上轴线{1,0}。
    removebottomspine (binary): 是否移除下轴线{1,0}。
    offset (numeric): 轴线距离图形的距离。
    trim (binary): 是否设置R风格轴线{1,0}。
    contextstyle (str): 图形元素大小风格调整{"paper", "notebook", "talk", "poster"}。
    matplotlibstyle (str): matplotlib支持的绘图风格{"Solarize_Light2", "_classic_test_patch", "_mpl-gallery", "_mpl-gallery-nogrid", "bmh", "classic", "dark_background", "fast", "fivethirtyeight", "ggplot", "grayscale", "seaborn-v0_8", "seaborn-v0_8-bright", "seaborn-v0_8-colorblind", "seaborn-v0_8-dark", "seaborn-v0_8-dark-palette", "seaborn-v0_8-darkgrid", "seaborn-v0_8-deep", "seaborn-v0_8-muted", "seaborn-v0_8-notebook", "seaborn-v0_8-paper", "seaborn-v0_8-pastel", "seaborn-v0_8-poster", "seaborn-v0_8-talk", "seaborn-v0_8-ticks", "seaborn-v0_8-white", "seaborn-v0_8-whitegrid", "tableau-colorblind10"}。
    barparamsdict (dict): 控制柱状误差图的参数字典。
    {
        estimator (str or callable): 估计量或者是用于估计每个分类下的统计函数{"mean", "median", "max", "min", "var", "std", "sum", callback}。
        errorbar (str): 误差估计量{"ci", "pi", "se", "sd", None}。
        n_boot (int): 计算置信区间误差估计量时使用到Bootstrap样本的数量。
        seed (int): Bootstrap估计时的随机数种子。
        orient (str): 柱状图的方向{"v", "h"}。
        color (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 柱子的填充颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        saturation (float): 颜色透明度。
        isfill (binary): 是否填充颜色{1,0}。
        width (numeric): 柱子的宽度。
        dodge (binary): 是否设置分组柱状图的排列方式为并排排列{1,0}。
        gap (numeric): 分组柱状图的排列方式为并排排列时柱子之间的间隔。
        islog (binary or positive numeric): 是否对数化(以10为底)后再绘制柱状图{1,0}或者是对数的底数。
        legend (str): 指定图例的样式{"auto", "brief", "full", False}。
        capsize (numeric): 误差条上短横线相对于柱子的宽度。
        isshowdatalabel (binary): 是否显示柱子高度或者长度的数据标签值{1,0}。
        datalabelsize (numeric): 数据标签字体大小。
        datalabelformat (str): 格式化数据标签值{"{:.2f}", "%g"}。
        datalabelcolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 数据标签的颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        errorbar_linewidth (numeric): errorbar线宽。
        errorbar_linecolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): errorbar线条的颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        errorbar_linestyle (str): errorbar线条的样式{"-", "--", "-.", ":"}。
    }

    返回值：
    Axes对象或者是Axes构成的二维数组

    示例：
    ===============================================================================0
    导入模块
    >>> import sys
    >>> sys.path.append(r"D:\document\statistics\TidyStatsProject")
    >>> from EasySeaborn import bar
    >>> import matplotlib.pyplot as plt
    >>> from SoEasyData import GetSeabornData
    >>> import numpy as np
    >>> penguins = GetSeabornData("penguins")
    >>> flights = GetSeabornData("flights")
    ===============================================================================1
    测试df参数(绘制整个dataframe中数值变量的估计量和误差值)
    >>> ax = bar(penguins, savefilename="./image/bar1.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================2
    测试df参数(某列的柱状图)
    >>> ax = bar(penguins["body_mass_g"], savefilename="./image/bar2.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================3
    测试xvarname参数(给定x轴数值变量，单个变量绘制水平柱状图)
    >>> ax = bar(penguins, xvarname="body_mass_g", savefilename="./image/bar3.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================4
    测试yvarname参数(给定y轴数值变量，单个变量绘制竖直柱状图)
    >>> ax = bar(penguins, yvarname="body_mass_g", savefilename="./image/bar4.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================5
    测试xvarname和yvarname参数(给定xy轴变量，一个字符一个数值，竖直分组柱状误差图)
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", savefilename="./image/bar5.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================6
    测试xvarname和yvarname参数(给定xy轴变量，一个字符一个数值，水平分组柱状误差图)
    >>> ax = bar(penguins, yvarname="island", xvarname="body_mass_g", savefilename="./image/bar6.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================7
    测试xvarname和yvarname参数(给定xy轴变量，两个数值，柱状图)
    >>> newpenguins = penguins.copy()
    >>> newpenguins["index"] = range(1, newpenguins.shape[0]+1)
    >>> ax = bar(newpenguins, xvarname="index", yvarname="body_mass_g", savefilename="./image/bar7.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================8
    测试groupby参数(给定XY变量下分组柱状图，颜色区分)
    >>> ax = bar(penguins, yvarname="island", xvarname="body_mass_g", groupby="island", savefilename="./image/bar8.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================9
    测试groupby参数(给定XY变量下分组柱状图，类别区分)
    >>> ax = bar(penguins, yvarname="island", xvarname="body_mass_g", groupby="sex", savefilename="./image/bar9.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================10
    测试一般绘图的标签参数
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, savefilename="./image/bar10.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================11
    测试colormap参数(分组柱状图指定颜色映射)
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", colormap="Set3", savefilename="./image/bar11.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================12
    测试colormap参数(分组柱状图指定颜色名称)
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", colormap=["red", "green"], savefilename="./image/bar12.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================13
    测试fig_length和fig_width参数(图形大小)
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", colormap="Set2", fig_length=6, fig_width=8, savefilename="./image/bar13.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================14
    测试layout参数(画布布局)
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", colormap="Set2", layout="tight", savefilename="./image/bar14.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", colormap="Set2", layout="constrained", savefilename="./image/bar15.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", colormap="Set2", layout="compressed", savefilename="./image/bar16.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", colormap="Set2", layout=None, savefilename="./image/bar17.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================15
    测试hue_order参数(分组变量中的顺序)
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", colormap="Set2", hue_order=["Male", "Female"], savefilename="./image/bar18.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", colormap="Set2", hue_order=["Female", "Male"], savefilename="./image/bar19.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================16
    测试order参数(柱子在X轴或者Y轴的排列顺序)
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", colormap="Set2", order=["Torgersen", "Biscoe", "Dream"], savefilename="./image/bar20.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", colormap="Set2", order=["Biscoe", "Torgersen", "Dream"], savefilename="./image/bar21.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", colormap="Set2", order=["Biscoe", "Dream", "Torgersen"], savefilename="./image/bar22.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================17
    测试fontfamily参数(指定字体样式)
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="方正舒体", savefilename="./image/bar23.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="方正姚体", savefilename="./image/bar24.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="仿宋", savefilename="./image/bar25.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="黑体", savefilename="./image/bar26.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="华文彩云", savefilename="./image/bar27.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="华文仿宋", savefilename="./image/bar28.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="华文琥珀", savefilename="./image/bar29.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="华文楷体", savefilename="./image/bar30.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="华文隶书", savefilename="./image/bar31.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="华文宋体", savefilename="./image/bar32.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="华文细黑", savefilename="./image/bar33.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="华文新魏", savefilename="./image/bar34.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="华文行楷", savefilename="./image/bar35.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="华文中宋", savefilename="./image/bar36.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="楷体", savefilename="./image/bar37.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="隶书", savefilename="./image/bar38.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="宋体", savefilename="./image/bar39.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="新宋体", savefilename="./image/bar40.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", savefilename="./image/bar41.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="year", ylabel="passengers", title="Bar Plot", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="TimesNewRoman", savefilename="./image/bar42.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", xlabel="year", ylabel="passengers", title="Bar Plot", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="Arial", savefilename="./image/bar43.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================18
    测试isshowplot参数(是否显示图形)
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", isshowplot=1, savefilename="./image/bar44.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", isshowplot=0, savefilename="./image/bar45.png", block=False)
    ===============================================================================19
    测试snsstyle参数(使用seaborn的风格)
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", snsstyle="darkgrid", savefilename="./image/bar46.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", snsstyle="whitegrid", savefilename="./image/bar47.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", snsstyle="dark", savefilename="./image/bar48.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", snsstyle="white", savefilename="./image/bar49.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", snsstyle="ticks", savefilename="./image/bar50.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================20
    测试isremoveleftspine参数(移除左轴线，snsstyle为ticks或者white时才有用)
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", snsstyle="white", removeleftspine=1, savefilename="./image/bar51.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", snsstyle="ticks", removeleftspine=0, savefilename="./image/bar52.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================21
    测试isremoverightspine参数(移除右轴线，snsstyle为ticks或者white时才有用)
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", snsstyle="white", removerightspine=1, savefilename="./image/bar53.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", snsstyle="ticks", removerightspine=0, savefilename="./image/bar54.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================22
    测试isremovetopspine参数(移除上轴线，snsstyle为ticks或者white时才有用)
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", snsstyle="white", removetopspine=1, savefilename="./image/bar55.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", snsstyle="ticks", removetopspine=0, savefilename="./image/bar56.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================23
    测试isremovebottomspine参数(移除下轴线，snsstyle为ticks或者white时才有用)
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", snsstyle="white", removebottomspine=1, savefilename="./image/bar57.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", snsstyle="ticks", removebottomspine=0, savefilename="./image/bar58.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================24
    测试offset参数(图形与轴线距离)
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", snsstyle="ticks", offset=3, savefilename="./image/bar59.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", offset=3, savefilename="./image/bar60.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================25
    测试trim参数(设置R风格轴线)
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", snsstyle="ticks", trim=1, savefilename="./image/bar61.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", trim=1, savefilename="./image/bar62.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================26
    测试contextstyle参数(绘图风格)
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", contextstyle="notebook", savefilename="./image/bar63.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", contextstyle="paper", savefilename="./image/bar64.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", contextstyle="talk", savefilename="./image/bar65.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", contextstyle="poster", savefilename="./image/bar66.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================27
    测试matplotlibstyle参数(matplotlib支持的绘图风格)
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="Solarize_Light2", savefilename="./image/bar67.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_classic_test_patch", savefilename="./image/bar68.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery", savefilename="./image/bar69.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery-nogrid", savefilename="./image/bar70.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="bmh", savefilename="./image/bar71.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="classic", savefilename="./image/bar72.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="dark_background", savefilename="./image/bar73.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fast", savefilename="./image/bar74.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fivethirtyeight", savefilename="./image/bar75.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="ggplot", savefilename="./image/bar76.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="grayscale", savefilename="./image/bar77.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8", savefilename="./image/bar78.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-bright", savefilename="./image/bar79.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-colorblind", savefilename="./image/bar80.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark", savefilename="./image/bar81.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark-palette", savefilename="./image/bar82.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-darkgrid", savefilename="./image/bar83.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-deep", savefilename="./image/bar84.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-muted", savefilename="./image/bar85.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-notebook", savefilename="./image/bar86.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-paper", savefilename="./image/bar87.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-pastel", savefilename="./image/bar88.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-poster", savefilename="./image/bar89.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-talk", savefilename="./image/bar90.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-ticks", savefilename="./image/bar91.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-white", savefilename="./image/bar92.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-whitegrid", savefilename="./image/bar93.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="tableau-colorblind10", savefilename="./image/bar94.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================28
    测试barparamsdict参数中estimator参数(估计量)
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "median"}, savefilename="./image/bar95.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "mean"}, savefilename="./image/bar96.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "max"}, savefilename="./image/bar97.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "min"}, savefilename="./image/bar98.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "var"}, savefilename="./image/bar99.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "std"}, savefilename="./image/bar100.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> r = lambda x: x.max()-x.min()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": r}, savefilename="./image/bar101.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================29
    测试barparamdict参数中的errorbar参数(指定误差)
    >>> ax = bar(penguins, yvarname="island", xvarname="body_mass_g", barparamsdict={"errorbar": "sd"}, savefilename="./image/bar102.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(penguins, yvarname="island", xvarname="body_mass_g", barparamsdict={"errorbar": "ci"}, savefilename="./image/bar103.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(penguins, yvarname="island", xvarname="body_mass_g", barparamsdict={"errorbar": "se"}, savefilename="./image/bar104.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(penguins, yvarname="island", xvarname="body_mass_g", barparamsdict={"errorbar": "pi"}, savefilename="./image/bar105.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================30
    测试barparamdict参数中的errorbar参数(不显示误差)
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum"}, savefilename="./image/bar106.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================31
    测试barparamdict参数中的n_boot参数(bootstrap方法估计置信区间的重抽样次数)
    >>> ax = bar(penguins, yvarname="island", xvarname="body_mass_g", barparamsdict={"errorbar": "ci", "n_boot": 2000}, savefilename="./image/bar107.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================32
    测试barparamdict参数中的seed参数(bootstrap方法估计置信区间的随机种子数)
    >>> ax = bar(penguins, yvarname="island", xvarname="body_mass_g", barparamsdict={"errorbar": "ci", "seed": 2}, savefilename="./image/bar108.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================33
    测试barparamdict参数中的orient参数(当xy都是数值变量时存在歧义，显示指定水平柱状误差图)
    >>> ax = bar(flights, xvarname="passengers", yvarname="year", barparamsdict={"orient": "h"}, savefilename="./image/bar109.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"orient": "v"}, savefilename="./image/bar110.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================34
    测试barparamdict参数中的color参数(填充颜色)
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"color": "red"}, savefilename="./image/bar111.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="island", barparamsdict={"color": "green"}, savefilename="./image/bar112.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"color": "blue"}, savefilename="./image/bar113.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================35
    测试barparamdict参数中的color参数(不填充颜色)
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"isfill": 0}, savefilename="./image/bar114.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================36
    测试barparamdict参数中的saturation参数(颜色饱和度)
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"color": "red", "saturation": 0.2}, savefilename="./image/bar115.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================37
    测试barparamdict参数中的width参数(设置柱子宽度)
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"width": 0.4}, savefilename="./image/bar116.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(flights, xvarname="year", yvarname="passengers", barparamsdict={"width": 1}, savefilename="./image/bar117.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================38
    测试barparamdict参数中的dodge参数(设置分组柱状图的排列方式)
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"dodge": 0}, savefilename="./image/bar118.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"dodge": 1}, savefilename="./image/bar119.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================39
    测试barparamdict参数中的gap参数(设置分组柱子之间的间距)
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"dodge": 1, "gap": 0.3}, savefilename="./image/bar120.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"dodge": 1, "gap": 0.1}, savefilename="./image/bar121.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"dodge": 0, "gap": 0.3}, savefilename="./image/bar122.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================40
    测试barparamdict参数中的gap参数(数据对数化)
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"islog": 0}, savefilename="./image/bar123.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"islog": 1}, savefilename="./image/bar124.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"islog": np.exp(1)}, savefilename="./image/bar125.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================41
    测试barparamdict参数中的legend参数(指定图例样式)
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"legend": "auto"}, savefilename="./image/bar126.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"legend": "brief"}, savefilename="./image/bar127.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"legend": "full"}, savefilename="./image/bar128.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"legend": False}, savefilename="./image/bar129.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================42
    测试barparamdict参数中的capsize参数(误差条上短横线相对于柱子的宽度)
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"capsize": 0.3}, savefilename="./image/bar130.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"capsize": 0.8}, savefilename="./image/bar131.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================43
    测试barparamdict参数中的isshowdatalabel参数(显示数据标签)
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"isshowdatalabel": 1}, savefilename="./image/bar132.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================44
    测试barparamdict参数中的datalabelsize,datalabelcolor,datalabelformat参数(数据标签格式)
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"isshowdatalabel": 1, "datalabelsize": 8, "datalabelformat": "{:.1f}", "datalabelcolor": "purple"}, savefilename="./image/bar133.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================45
    测试barparamdict参数中的errorbar_linewidth,errorbar_linecolor,errorbar_linestyle参数(errorbar样式)
    >>> ax = bar(penguins, xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"errorbar_linestyle": "-.", "errorbar_linecolor": "purple", "errorbar_linewidth": 0.5}, savefilename="./image/bar134.png", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================46
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
    barparamsdictdefault = {
        "estimator": "mean",
        "errorbar": (
            "ci",
            95),
        "n_boot": 1000,
        "seed": None,
        "orient": None,
        "color": None,
        "saturation": 0.75,
        "isfill": 1,
        "width": 0.8,
        "dodge": "auto",
        "gap": 0,
        "islog": 0,
        "legend": "auto",
        "capsize": 0,
        "isshowdatalabel": 0,
        "datalabelsize": 10,
        "datalabelformat": "%g",
        "datalabelcolor": "black",
        "errorbar_linewidth": 1,
        "errorbar_linecolor": "black",
        "errorbar_linestyle": "-"}
    # 更新字典
    barparamsdictdefault.update(barparamsdict)
    if matplotlibstyle is None:
        with sns.axes_style(snsstyle):
            sns.set_context(contextstyle)
            # 开始绘图，画布参数
            fig, ax = plt.subplots(
                figsize=(fig_length, fig_width), layout=layout)
            # 核心变量参数，颜色参数，图形参数
            ax = sns.barplot(data=df, x=xvarname, y=yvarname, hue=groupby, ax=ax, palette=colormap,
                                hue_order=hue_order, order=order, estimator=barparamsdictdefault[
                                    "estimator"],
                                errorbar=barparamsdictdefault["errorbar"], n_boot=barparamsdictdefault["n_boot"],
                                seed=barparamsdictdefault["seed"], orient=barparamsdictdefault["orient"],
                                color=barparamsdictdefault["color"], saturation=barparamsdictdefault["saturation"],
                                fill=bool(barparamsdictdefault["isfill"]), width=barparamsdictdefault["width"],
                                dodge=barparamsdictdefault["dodge"], gap=barparamsdictdefault["gap"],
                                log_scale=bool(barparamsdictdefault["islog"]) if barparamsdictdefault[
                                    "islog"] == 0 or barparamsdictdefault["islog"] == 1 else barparamsdictdefault["islog"],
                                legend=barparamsdictdefault["legend"], capsize=barparamsdictdefault["capsize"],
                                err_kws={"linestyle": barparamsdictdefault["errorbar_linestyle"], "color": barparamsdictdefault[
                                    "errorbar_linecolor"], "linewidth": barparamsdictdefault["errorbar_linewidth"]}
                                )
            if bool(barparamsdictdefault["isshowdatalabel"]):
                ax.bar_label(
                    ax.containers[0],
                    fontsize=barparamsdictdefault["datalabelsize"],
                    fmt=barparamsdictdefault["datalabelformat"],
                    color=barparamsdictdefault["datalabelcolor"])
    else:
        with plt.style.context(matplotlibstyle):
            # 开始绘图，画布参数
            fig, ax = plt.subplots(
                figsize=(fig_length, fig_width), layout=layout)
            # 核心变量参数，颜色参数，图形参数
            ax = sns.barplot(data=df, x=xvarname, y=yvarname, hue=groupby, ax=ax, palette=colormap,
                                hue_order=hue_order, order=order, estimator=barparamsdictdefault[
                                    "estimator"],
                                errorbar=barparamsdictdefault["errorbar"], n_boot=barparamsdictdefault["n_boot"],
                                seed=barparamsdictdefault["seed"], orient=barparamsdictdefault["orient"],
                                color=barparamsdictdefault["color"], saturation=barparamsdictdefault["saturation"],
                                fill=bool(barparamsdictdefault["isfill"]), width=barparamsdictdefault["width"],
                                dodge=barparamsdictdefault["dodge"], gap=barparamsdictdefault["gap"],
                                log_scale=bool(barparamsdictdefault["islog"]) if barparamsdictdefault[
                                    "islog"] == 0 or barparamsdictdefault["islog"] == 1 else barparamsdictdefault["islog"],
                                legend=barparamsdictdefault["legend"], capsize=barparamsdictdefault["capsize"],
                                err_kws={"linestyle": barparamsdictdefault["errorbar_linestyle"], "color": barparamsdictdefault[
                                    "errorbar_linecolor"], "linewidth": barparamsdictdefault["errorbar_linewidth"]}
                                )
            if bool(barparamsdictdefault["isshowdatalabel"]):
                ax.bar_label(
                    ax.containers[0],
                    fontsize=barparamsdictdefault["datalabelsize"],
                    fmt=barparamsdictdefault["datalabelformat"],
                    color=barparamsdictdefault["datalabelcolor"])
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
