from altair import Chart, Tooltip
from pandas import DataFrame
from app.data import MonsterDatabase

def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:

    graph = Chart(
        df,
        title = f"{y} by {x} for {target}"
    ).mark_circle(size=50).encode(
        x=x,
        y=y,
        color=target,
        tooltip = Tooltip(df.columns.to_list())
    ).configure_title(
        font="Helvetica Neue",
        fontSize=20,
        color="black",
        anchor="middle"
    ).configure_axis(
        grid=True,
        gridColor="black",
        labelFont="Helvetica Neue",
        labelFontSize=10,
        labelColor="black",
        titleFont="Helvetica Neue",
        titleFontSize=14,
        titleColor="black"
    )
    return graph