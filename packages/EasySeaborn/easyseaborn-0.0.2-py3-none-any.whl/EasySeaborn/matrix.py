import matplotlib.pyplot as plt
from matplotlib import font_manager
from pathlib import Path
import seaborn as sns
import warnings
# 禁用警告
warnings.filterwarnings("ignore")

# 获取包所在的路径
current_PACKAGE_PATH = Path(__file__).resolve().parent


def matrix(
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
        matrixparamsdict={
            "vars": None,
            "x_vars": None,
            "y_vars": None,
            "iscorner": 0,
            "mainwhichplot": None,
            "subwhichplot": None,
            "upperwhichplot": None,
            "lowerwhichplot": None,
            "islegend": 0,
            "title": None,
            "issharediagy": 1},
        **kwargs):
    """
    这是一个Seaborn绘制矩阵散点图函数的文档字符串。

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
    matrixparamsdict (dict): 控制矩阵图的参数字典。
    {
        vars (list or str): 矩阵图中要展示的变量信息。
        x_vars (list of str): 行变量。
        y_vars (list of str): 列变量。
        iscorner (binary): 是否绘制下三角矩阵图。
        mainwhichplot (str): 非主对角线上绘制什么图形{"scatter", "kde"}。
        subwhichplot (str): 主对角线上绘制什么图形{"hist", "kde", "box", "violin", "jitter", "ecdf"}。
        upperwhichplot (str): 上三角绘制什么图形{"scatter", "kde"}。
        lowerwhichplot (str): 下三角绘制什么图形{"scatter", "kde"}。
        islegend (binary): 是否绘制图例{1,0}。
        title (str): 图形总标题。
        issharediagy (binary): 是否共享对角线上图形的Y轴坐标{1,0}。
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
    ===============================================================================229
    测试matrix矩阵图参数
    ===============================================================================230
    对角线上没有设置
    >>> ax = TidySeabornFlexible(penguins, "matrix", block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================231
    设置对角线为直方图
    >>> ax = TidySeabornFlexible(penguins, "matrix", matrixparamsdict={"subwhichplot": "hist"}, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================232
    设置上三角和下三角为不同的图
    >>> ax = TidySeabornFlexible(penguins, "matrix", matrixparamsdict={"subwhichplot": "kde", "upperwhichplot": "scatter", "lowerwhichplot": "kde", "issharediagy": 0}, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================233
    下三角矩阵图
    >>> ax = TidySeabornFlexible(penguins, "matrix", matrixparamsdict={"subwhichplot": "kde", "lowerwhichplot": "scatter", "issharediagy": 0, "iscorner": 1}, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================234
    分组矩阵散点图
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde"}, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================235
    设置对角线为箱线图
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "box"}, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================236
    设置对角线为核密度估计图
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde"}, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================237
    设置对角线为小提琴图
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "violin"}, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================238
    设置对角线为抖动图
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "jitter"}, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================239
    设置对角线为经验分布函数图
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "ecdf"}, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================240
    添加图例
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================241
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, savefilename="./image/矩阵散点图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================242
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================243
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================286
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
    matrixparamsdictdefault = {
        "vars": None,
        "x_vars": None,
        "y_vars": None,
        "iscorner": 0,
        "mainwhichplot": None,
        "subwhichplot": None,
        "upperwhichplot": None,
        "lowerwhichplot": None,
        "islegend": 0,
        "title": None,
        "issharediagy": 1}
    # 更新字典
    matrixparamsdictdefault.update(matrixparamsdict)
    subwhichplotdict = {
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
            facet = sns.PairGrid(
                data=df,
                hue=groupby,
                palette=colormap,
                hue_order=hue_order,
                height=fig_width if fig_width == 2.5 else 2.5,
                aspect=fig_length /
                fig_width if fig_length /
                fig_width == 1 else 1,
                vars=matrixparamsdictdefault["vars"],
                x_vars=matrixparamsdictdefault["x_vars"],
                y_vars=matrixparamsdictdefault["y_vars"],
                corner=bool(
                    matrixparamsdictdefault["iscorner"]),
                diag_sharey=bool(
                    matrixparamsdictdefault["issharediagy"]))
            if matrixparamsdictdefault["subwhichplot"] is not None:
                facet.map_diag(
                    subwhichplotdict[matrixparamsdictdefault["subwhichplot"]])
                if matrixparamsdictdefault["mainwhichplot"] is None:
                    if matrixparamsdictdefault["upperwhichplot"] is not None and matrixparamsdictdefault["lowerwhichplot"] is not None:
                        facet.map_upper(
                            sns.scatterplot if matrixparamsdictdefault["upperwhichplot"] == "scatter" else sns.kdeplot)
                        facet.map_lower(
                            sns.scatterplot if matrixparamsdictdefault["lowerwhichplot"] == "scatter" else sns.kdeplot)
                    else:
                        facet.map_offdiag(sns.scatterplot)
                else:
                    facet.map_offdiag(
                        sns.scatterplot if matrixparamsdictdefault[
                            "mainwhichplot"] == "scatter" else sns.kdeplot
                    )
            else:
                if matrixparamsdictdefault["mainwhichplot"] is None:
                    if matrixparamsdictdefault["upperwhichplot"] is not None and matrixparamsdictdefault["lowerwhichplot"] is not None:
                        facet.map_upper(
                            sns.scatterplot if matrixparamsdictdefault["upperwhichplot"] == "scatter" else sns.kdeplot)
                        facet.map_lower(
                            sns.scatterplot if matrixparamsdictdefault["lowerwhichplot"] == "scatter" else sns.kdeplot)
                    else:
                        facet.map(sns.scatterplot)
                else:
                    facet.map_offdiag(
                        sns.scatterplot if matrixparamsdictdefault[
                            "mainwhichplot"] == "scatter" else sns.kdeplot
                    )
            if bool(matrixparamsdictdefault["islegend"]):
                facet.add_legend()
            else:
                pass
    else:
        with plt.style.context(matplotlibstyle):
            # 核心变量参数，颜色参数，图形参数
            facet = sns.PairGrid(
                data=df,
                hue=groupby,
                palette=colormap,
                hue_order=hue_order,
                height=fig_width if fig_width == 2.5 else 2.5,
                aspect=fig_length /
                fig_width if fig_length /
                fig_width == 1 else 1,
                vars=matrixparamsdictdefault["vars"],
                x_vars=matrixparamsdictdefault["x_vars"],
                y_vars=matrixparamsdictdefault["y_vars"],
                corner=bool(
                    matrixparamsdictdefault["iscorner"]),
                diag_sharey=bool(
                    matrixparamsdictdefault["issharediagy"]))
            if matrixparamsdictdefault["subwhichplot"] is not None:
                facet.map_diag(
                    subwhichplotdict[matrixparamsdictdefault["subwhichplot"]])
                if matrixparamsdictdefault["mainwhichplot"] is None:
                    if matrixparamsdictdefault["upperwhichplot"] is not None and matrixparamsdictdefault["lowerwhichplot"] is not None:
                        facet.map_upper(
                            sns.scatterplot if matrixparamsdictdefault["upperwhichplot"] == "scatter" else sns.kdeplot)
                        facet.map_lower(
                            sns.scatterplot if matrixparamsdictdefault["lowerwhichplot"] == "scatter" else sns.kdeplot)
                    else:
                        facet.map_offdiag(sns.scatterplot)
                else:
                    facet.map_offdiag(
                        sns.scatterplot if matrixparamsdictdefault[
                            "mainwhichplot"] == "scatter" else sns.kdeplot
                    )
            else:
                if matrixparamsdictdefault["mainwhichplot"] is None:
                    if matrixparamsdictdefault["upperwhichplot"] is not None and matrixparamsdictdefault["lowerwhichplot"] is not None:
                        facet.map_upper(
                            sns.scatterplot if matrixparamsdictdefault["upperwhichplot"] == "scatter" else sns.kdeplot)
                        facet.map_lower(
                            sns.scatterplot if matrixparamsdictdefault["lowerwhichplot"] == "scatter" else sns.kdeplot)
                    else:
                        facet.map(sns.scatterplot)
                else:
                    facet.map_offdiag(
                        sns.scatterplot if matrixparamsdictdefault[
                            "mainwhichplot"] == "scatter" else sns.kdeplot
                    )
            if bool(matrixparamsdictdefault["islegend"]):
                facet.add_legend()
            else:
                pass
    fig = facet.fig
    axes = facet.axes
    # 移除spines
    sns.despine(
        left=removeleftspine,
        right=removerightspine,
        top=removetopspine,
        bottom=removebottomspine,
        offset=offset,
        trim=trim)
    if matrixparamsdictdefault["title"] is not None:
        plt.suptitle(
            matrixparamsdictdefault["title"], fontproperties=fontobj)
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
