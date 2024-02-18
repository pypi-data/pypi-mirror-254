import matplotlib.pyplot as plt
from matplotlib import font_manager
from pathlib import Path
import seaborn as sns
import warnings
# 禁用警告
warnings.filterwarnings("ignore")

# 获取包所在的路径
current_PACKAGE_PATH = Path(__file__).resolve().parent


def joint(
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
        jointparamsdict={
            "margin_plottype": "hist",
            "margin_x_plottype": None,
            "margin_y_plottype": None,
            "space": 0.2,
            "isdropna": 0,
            "xlim": None,
            "ylim": None,
            "isshowmargin_ticks": 0,
            "title": None},
        **kwargs):
    """
    这是一个Seaborn绘制联合图函数的文档字符串。

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
    jointparamsdict (dict): 控制联合边际图的参数字典。
    {
        margin_plottype (str): 边际图的类型{"hist", "box", "violin", "jitter", "kde", "ecdf"}。
        margin_x_plottype (str): 投影到X轴上的边际图的类型{"hist", "box", "violin", "jitter", "kde", "ecdf"}。
        margin_y_plottype (str): 投影到Y轴上边际图的类型{"hist", "box", "violin", "jitter", "kde", "ecdf"}。
        space (numeric): 联合图和边际图之间的间距。
        isdropna (binary): 是否删除缺失值再画图{1,0}。
        xlim (tuple): X轴范围。
        ylim (tuple): Y轴范围。
        isshowmargin_ticks (binary): 是否显示边际图的刻度{1,0}。
        title (str): 图形总标题。
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
    测试直方图参数
    ===============================================================================244
    测试联合图
    ===============================================================================245
    边际直方图
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================246
    边际箱线图
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_plottype": "box"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================247
    边际小提琴图
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_plottype": "violin"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================248
    边际核密度估计图
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_plottype": "kde"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================249
    边际抖动图
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_plottype": "jitter"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================250
    边际经验分布函数图
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_plottype": "ecdf"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================251
    设置X和Y不同边际图
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_x_plottype": "ecdf", "margin_y_plottype": "box"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_x_plottype": "ecdf", "margin_y_plottype": "violin"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_x_plottype": "ecdf", "margin_y_plottype": "jitter"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_x_plottype": "ecdf", "margin_y_plottype": "kde"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_x_plottype": "kde", "margin_y_plottype": "box"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_x_plottype": "kde", "margin_y_plottype": "violin"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_x_plottype": "kde", "margin_y_plottype": "jitter"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_x_plottype": "box", "margin_y_plottype": "violin"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_x_plottype": "box", "margin_y_plottype": "jitter"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================252
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, savefilename="./image/联合分布图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================253
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================254
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================255
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
    jointparamsdictdefault = {
        "margin_plottype": "hist",
        "margin_x_plottype": None,
        "margin_y_plottype": None,
        "space": 0.2,
        "isdropna": 0,
        "xlim": None,
        "ylim": None,
        "isshowmargin_ticks": 0,
        "title": None}
    # 更新字典
    jointparamsdictdefault.update(jointparamsdict)
    marginplotdict = {
        "hist": sns.histplot,
        "kde": sns.kdeplot,
        "box": sns.boxplot,
        "violin": sns.violinplot,
        "jitter": sns.stripplot,
        "ecdf": sns.ecdfplot
    }
    if matplotlibstyle is None:
        with sns.axes_style(snsstyle):
            sns.set_context(contextstyle)
            # 核心变量参数，颜色参数，图形参数
            facet = sns.JointGrid(
                data=df,
                x=xvarname,
                y=yvarname,
                hue=groupby,
                palette=colormap,
                hue_order=hue_order,
                height=fig_width if fig_width == 6 else 6,
                ratio=5,
                xlim=jointparamsdictdefault["xlim"],
                ylim=jointparamsdictdefault["ylim"],
                dropna=bool(
                    jointparamsdictdefault["isdropna"]),
                marginal_ticks=bool(
                    jointparamsdictdefault["isshowmargin_ticks"]))
            if jointparamsdictdefault["margin_x_plottype"] is not None and jointparamsdictdefault["margin_y_plottype"] is not None:
                ax_x = facet.ax_marg_x
                ax_y = facet.ax_marg_y
                sns.scatterplot(data=df, x=xvarname,
                                y=yvarname, ax=facet.ax_joint)
                marginplotdict[jointparamsdictdefault["margin_x_plottype"]](
                    data=df, x=xvarname, ax=ax_x)
                marginplotdict[jointparamsdictdefault["margin_y_plottype"]](
                    data=df, y=yvarname, ax=ax_y)
            else:
                facet.plot(
                    sns.scatterplot, marginplotdict[jointparamsdictdefault["margin_plottype"]])

    else:
        with plt.style.context(matplotlibstyle):
            # 核心变量参数，颜色参数，图形参数
            facet = sns.JointGrid(
                data=df,
                x=xvarname,
                y=yvarname,
                hue=groupby,
                palette=colormap,
                hue_order=hue_order,
                height=fig_width if fig_width == 6 else 6,
                ratio=5,
                xlim=jointparamsdictdefault["xlim"],
                ylim=jointparamsdictdefault["ylim"],
                dropna=bool(
                    jointparamsdictdefault["isdropna"]),
                marginal_ticks=bool(
                    jointparamsdictdefault["isshowmargin_ticks"]))
            if jointparamsdictdefault["margin_x_plottype"] is not None and jointparamsdictdefault["margin_y_plottype"] is not None:
                ax_x = facet.ax_marg_x
                ax_y = facet.ax_marg_y
                sns.scatterplot(data=df, x=xvarname,
                                y=yvarname, ax=facet.ax_joint)
                marginplotdict[jointparamsdictdefault["margin_x_plottype"]](
                    data=df, x=xvarname, ax=ax_x)
                marginplotdict[jointparamsdictdefault["margin_y_plottype"]](
                    data=df, y=yvarname, ax=ax_y)
            else:
                facet.plot(
                    sns.scatterplot, marginplotdict[jointparamsdictdefault["margin_plottype"]])
    fig = facet.figure
    # 移除spines
    sns.despine(
        left=removeleftspine,
        right=removerightspine,
        top=removetopspine,
        bottom=removebottomspine,
        offset=offset,
        trim=trim)
    if jointparamsdictdefault["title"] is not None:
        plt.suptitle(
            jointparamsdictdefault["title"], fontproperties=fontobj)
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
    return fig
