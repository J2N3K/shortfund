import pandas as pd
import plotly.express as px
from shiny import App, ui, render
from shinywidgets import render_widget, output_widget
from pathlib import Path

import icons, markdown_content, outstanding_shares, tickers

PATH = r'2025-02-28 00-51-57 Lista Pozycji RSS.xlsx'
df = pd.read_excel(PATH, header=1, index_col="Lp.")

STOCKS_LIST = list(df['Nazwa papieru'].unique())
STOCKS_N = df['Nazwa papieru'].nunique()
SELLERS_LIST = list(df['Posiadacz pozycji krótkiej'].unique())
SELLERS_N = df['Posiadacz pozycji krótkiej'].nunique()


app_ui = ui.page_fluid(
    ui.page_navbar(
        ui.nav_panel("Wykresy",
            ui.div(
                icons.alert, 
                " Cześć! Strona nadal jest w budowie, więc mogą występować drobne problemy - szczególnie na urządzeniach mobilnych.",
                class_="alert alert-info"
            ),
            
            ui.input_select('stock_id', "Wybierz spółkę:", STOCKS_LIST),
            ui.layout_columns(
                ui.navset_card_underline(
                    ui.nav_panel(" Wykres", output_widget("barplot1"), icon=icons.chart),
                    ui.nav_panel(" Tabela", ui.output_data_frame("summary1"), icon=icons.table)
                ),
                ui.card(
                    ui.HTML(f'<div style="text-align: center;"> Liczba pożyczonych akcji [%] <h1><b> {ui.output_text('shorts_sum')} </b></h1>co odpowiada około <b> {ui.output_text('shares_calc')} </b> wszystkich akcji</div>'),
                    ui.output_ui('stocks_img')
                ),
                col_widths=[8,4], row_heights='60vh'
            ),

            ui.layout_columns(  
                ui.value_box(
                    "Shortowanych jest",
                    STOCKS_N,
                    "spółek z warszawskiego parkietu",
                    theme="text-green",
                    showcase=icons.graph_down,
                ),
                ui.value_box(
                    "Liczba funduszy grających na spadki wynosi:",
                    SELLERS_N,
                    showcase=icons.users,
                ),
                ui.value_box(
                    "Ostatnia aktualizacja danych:",
                    PATH[-42:-23],
                    showcase=icons.radio,
                    theme="text-blue",
                )
            ),
            
            ui.input_select('fund_id', "Wybierz fundusz:", SELLERS_LIST),
            ui.layout_columns(
                ui.navset_card_underline(
                    ui.nav_panel(" Wykres", output_widget("barplot2"), icon=icons.chart),
                    ui.nav_panel(" Tabela", ui.output_data_frame("summary2"), icon=icons.table)
                ),
                row_heights='60vh'
            ),

            ui.markdown('---'),
            ui.layout_columns(
                ui.markdown('<script type="text/javascript" src="https://static.stooq.com/pp/gc.js"></script>'),
                ui.markdown('<script type="text/javascript" src="https://static.stooq.com/pp/wc.js"></script>'),
                ui.markdown('<script type="text/javascript" src="https://static.stooq.com/pp/cc.js"></script>'),
                gap=100
            ),
        ),
        
        ui.nav_panel("O projekcie", ui.markdown(markdown_content.markdown)),        
        
        navbar_options=ui.navbar_options(
            bg="#aaaaaa",
        ),
        title=ui.img(src="logo1.png", style="max-height:40px;)"),
        footer=ui.HTML("<div style='text-align:center; background-color: #003366; padding: 5px; border-top-right-radius: 15px; border-top-left-radius: 15px'><span style=color:#ffffff;> janek © 2025 </span></div>"),
        fluid=False,
    ),
    ui.tags.link(rel="icon", href="favicon.png"),
    title='Shortfund',
    #theme=theme,
)

def server(input, output, session):    
    @render_widget
    def barplot1():
        fig1=px.bar(
            df.loc[df['Nazwa papieru'] == input.stock_id()],
            x='Posiadacz pozycji krótkiej',
            y='Pozycja krótka netto (%)',
            title=f'Podmioty z pozycją krótką na spółce <b>{input.stock_id()}</b>',
            text_auto=True,
        )
        return fig1
    
    @render.data_frame
    def summary1():
        return render.DataGrid(df.loc[df['Nazwa papieru'] == input.stock_id()])
    
    @render.text
    def shorts_sum():
        return sum((df.loc[df['Nazwa papieru']==input.stock_id(), 'Pozycja krótka netto (%)']))
    
    @render.text
    def shares_calc():
        val = sum((df.loc[df['Nazwa papieru']==input.stock_id(), 'Pozycja krótka netto (%)']))
        val = val/100 * outstanding_shares.outstanding_shares[input.stock_id()]
        return f'{val:,.0f}'
        
    @render.ui
    def stocks_img():
        link = f'https://stooq.com/c/?p&s={tickers.stocks[input.stock_id()]}&c=1d'
        return ui.p(ui.markdown(f'<div style="text-align: center;"><a href="https://stooq.com/q/?s={tickers.stocks[input.stock_id()]}"><img src="{link}"></img></div>'))

    @render_widget
    def barplot2():
        fig2=px.bar(
            df.loc[df['Posiadacz pozycji krótkiej'] == input.fund_id()],
            x='Nazwa papieru',
            y='Pozycja krótka netto (%)',
            title=f'Portfolio funduszu <b>{input.fund_id()}</b>',
            text_auto=True,
            color='Nazwa papieru',
        )
        return fig2
    
    @render.data_frame
    def summary2():
        return render.DataGrid(df.loc[df['Posiadacz pozycji krótkiej'] == input.fund_id()])
    

app = App(app_ui, server, static_assets=Path(__file__).parent / 'www')
