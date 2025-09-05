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
    )
    return graph