import flet as ft
import requests
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

API_URL = "http://localhost:3000/produtos"

def pesquisa(page: ft.Page):
    txt_pesq_marca = ft.TextField(label="Pesquisar por Marca", expand=2)
    txt_pesq_preco = ft.TextField(label="Preço Máximo (R$)", expand=2)
    tabela_ref = ft.Ref[ft.DataTable]()

    tabela = ft.DataTable(
        ref=tabela_ref,
        columns=[
            ft.DataColumn(ft.Text("Cód.")),
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Marca")),
            ft.DataColumn(ft.Text("Quant.")),
            ft.DataColumn(ft.Text("Preço R$")),
        ],
        rows=[],
    )

    def pesquisar_click(e):
        marca_filtro = txt_pesq_marca.value.strip().lower()
        preco_filtro = txt_pesq_preco.value.strip().replace(",", ".")

        try:
            preco_filtro = float(preco_filtro) if preco_filtro else None
        except ValueError:
            page.snack_bar.content = ft.Text("Preço inválido.")
            page.snack_bar.open = True
            page.update()
            return

        try:
            response = requests.get(API_URL)
            response.raise_for_status()
            produtos = response.json()

            filtrados = []
            for p in produtos:
                preco_valor = float(p["preco"])
                marca_ok = marca_filtro in p["marca"].lower() if marca_filtro else True
                preco_ok = preco_valor <= preco_filtro if preco_filtro is not None else True

                if marca_ok and preco_ok:
                    filtrados.append(p)

            tabela_ref.current.rows.clear()
            for p in reversed(filtrados):
                preco_valor = float(p["preco"])
                preco_f = locale.currency(preco_valor, grouping=True)
                tabela_ref.current.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(p["id"]))),
                    ft.DataCell(ft.Text(p["nome"])),
                    ft.DataCell(ft.Text(p["marca"])),
                    ft.DataCell(ft.Text(str(p["quant"]))),
                    ft.DataCell(ft.Text(preco_f)),
                ]))
            page.update()

        except Exception as err:
            page.snack_bar.content = ft.Text(f"Erro ao buscar: {err}")
            page.snack_bar.open = True
            page.update()

    layout = ft.Column([
        ft.Text("Pesquisa de Produtos", size=24, weight="bold"),
        ft.Row([txt_pesq_marca, txt_pesq_preco, ft.ElevatedButton("Pesquisar", on_click=pesquisar_click)], spacing=10),
        ft.Divider(),
        ft.Container(
            content=tabela,
            height=400,
            padding=5,
            border=ft.border.all(1, ft.Colors.GREY_300),
            border_radius=10,
            bgcolor=ft.Colors.GREY_100
        )
    ], spacing=10)

    return layout
