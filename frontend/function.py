import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
def market_overview(df):
    total_trading_volume = df['TtlTradgVol'].sum()
    total_no_txn=df['TtlNbOfTxsExctd'].sum()
    total_trf_value=df['TtlTrfVal'].sum()
    #profit or loss 
    advancing=(df['ClsPric']>df['PrvsClsgPric']).sum()
    declining=(df['ClsPric']<df['PrvsClsgPric']).sum()
    unchanged=(df['ClsPric']==df['PrvsClsgPric']).sum()
    #plot-visualisation
    company_volume = np.sort(np.array(df.groupby("FinInstrmNm")["TtlTradgVol"].sum()))
    top_volume=company_volume[-10:][::-1]
    names=df.groupby("FinInstrmNm")["TtlTradgVol"].sum().nlargest(10).index
    fig,ax=plt.subplots(figsize=(10, 10),
    dpi=150
)

    fig.patch.set_alpha(0)
    ax.patch.set_alpha(0)

    ax.barh(names,top_volume)
    ax.set_xlabel('Trading Volume x 10^8')
    ax.set_ylabel('Company Names')
    
   
    plt.tight_layout() 
    #market returns
    closing_prices = np.array(df['ClsPric'])
    previous_closing_prices = np.array(df['PrvsClsgPric'])
    market_returns = (closing_prices - previous_closing_prices)*100 / previous_closing_prices
    companies=np.array(df['FinInstrmNm'])
    idx=np.argmax(market_returns)
    companies[idx]
    sorted_return=market_returns.argsort()
    top_10=sorted_return[-10:][::-1]
    
    bottom_10=sorted_return[:10]
    top_return=pd.DataFrame({"company":companies[top_10]
                ,"return":market_returns[top_10]
                })
    bottom_return=pd.DataFrame({"company":companies[bottom_10],
                                "return":market_returns[bottom_10]})
    company = df.loc[df["TtlTradgVol"].idxmax(), "FinInstrmNm"]
    volume = df["TtlTradgVol"].max()
    company_txn=df.loc[df["TtlNbOfTxsExctd"].idxmax(), "FinInstrmNm"]
    volume2=df["TtlNbOfTxsExctd"].max()
    trf_highest=df.loc[df["TtlTrfVal"].idxmax(), "FinInstrmNm"]
    volume3=df["TtlTrfVal"].max()
    
    txn=df['TtlTradgVol'][df['TtlNbOfTxsExctd'].argmax()]
    trf_value=df['TtlNbOfTxsExctd'][df['TtlTrfVal'].argmax()]

    #canlde stick
    stocks=companies[top_10]
    candle_fig={}
    for stock in stocks:
        stock_data=df[df["FinInstrmNm"]==stock]
        candle_fig[stock]=go.Figure(
            data=[
                go.Candlestick(
                x=stock_data["TradDt"],
                open=stock_data["OpnPric"],
                high=stock_data["HghPric"],
                low=stock_data["LwPric"],
                close=stock_data["ClsPric"]
                )
            ]
        )
    #pie
    labels=['advancing','declining','unchanged']
    values=[advancing,declining,unchanged]
    pie_fig,pie_ax=plt.subplots(figsize=(3,3),dpi=150)
    pie_ax.pie(
        values,
        labels=labels,
            autopct='%1.1f%%',
    startangle=90
)

    pie_ax.set_title("Market Breadth")

    plt.tight_layout()

    

    return total_no_txn,total_trading_volume,total_trf_value,fig,top_return,bottom_return,advancing,declining,unchanged,company,volume,volume2,volume3,trf_highest,company_txn,stocks,candle_fig,pie_fig
    