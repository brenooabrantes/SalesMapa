import folium
import webbrowser

def gerar_lista_pontos(pontos_cameras, pontos_wifi): # Ordenar os pontos / Use de acordo com sua necessidade

    # Combina as listas de pontos
    todos_pontos = [{"tipo": "Câmera", **p} for p in pontos_cameras] + [{"tipo": "Wi-Fi", **p} for p in pontos_wifi]

    # Ordena por número
    todos_pontos_ordenados = sorted(todos_pontos, key=lambda x: x["numero"])

    # Gera a lista formatada
    lista_formatada = [
        f"{p['numero']}: {p['nome']} ({p['tipo']})" for p in todos_pontos_ordenados
    ]

    return lista_formatada

def calcular_ponto_medio(pontos_wifi, numeros_selecionados): # Função para encontrar pontos médios

    # Filtra os pontos escolhidos com base no número
    pontos_selecionados = [p for p in pontos_wifi if p['numero'] in numeros_selecionados]

    if not pontos_selecionados:
        raise ValueError("Nenhum ponto correspondente encontrado nos números fornecidos.")

    # Calcula a média das latitudes e longitudes
    media_lat = sum(p['coords'][0] for p in pontos_selecionados) / len(pontos_selecionados)
    media_lon = sum(p['coords'][1] for p in pontos_selecionados) / len(pontos_selecionados)

    return [media_lat, media_lon]


cidade_coords = [-00.000, -00.000]  # Ajuste para sua cidade



pontos_x = [  # Utilize de acordo com sua necessidade
    {"nome": "XXX-XXX", "coords": [-00.000, -00.000], "numero": 1},
]

pontos_y = [
    {"nome": "XXX-XXX", "coords": [-00.000, -00.000], "numero": 1},

]

mapa = folium.Map(location=cidade_coords, zoom_start=14, tiles="CartoDB positron",
                  zoom_control=True)

# Forma de visualização do mapa padrão
folium.TileLayer(
    tiles="CartoDB positron",
    name="Mapa Padrão",
    overlay=False,
    control=True,
).add_to(mapa)

# Forma de visualização do mapa Esri
folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Esri",
    name="Satélite",
    overlay=False,
    control=True,
).add_to(mapa)

# Adicionar controle de camadas ao mapa
folium.LayerControl(collapsed=False).add_to(mapa)

for ponto in pontos_x:
    folium.Marker(
        location=ponto["coords"],
        icon=folium.Icon(color="red", icon="camera")  # Ícone de câmeras / Use com base na sua necessidade
    ).add_to(mapa)

    folium.map.Marker(
        location=ponto["coords"],
        icon=folium.DivIcon(
            html=f"""<div style="font-size: 18px; color: purple;"><b>{ponto['numero']}</div>""" # Utilizar a fonte de acordo com sua necessidade
        )
    ).add_to(mapa)

for ponto in pontos_y:
    folium.Marker(
        location=ponto["coords"],
        icon=folium.Icon(color="blue", icon="cloud")  # Ícone de Wi-Fi / Use com base na sua necessidade
    ).add_to(mapa)

    folium.map.Marker(
        location=ponto["coords"],
        icon=folium.DivIcon(
            html=f"""<div style="font-size: 18px; color: purple;"><b>{ponto['numero']}</b></div>""" # Utilizar a fonte de acordo com sua necessidade
        )
    ).add_to(mapa)

lista_pontos = gerar_lista_pontos(pontos_x, pontos_y)

# Salvar e abrir o mapa
nome_arquivo = "xxx.html"
mapa.save(nome_arquivo)

legend_html = '''
<div style="
    position: fixed;
    bottom: 50px;
    left: 50px;
    width: 200px;
    background-color: white;
    border: 2px solid black;
    padding: 10px;
    font-size: 14px;
    z-index: 9999;
    ">
    <b>Legenda:</b><br>
    <i class="fa fa-camera" style="color:red"></i> Câmeras<br>
    <i class="fa fa-cloud" style="color:blue"></i> Wi-Fi<br>
</div>
'''

scale_html = '''
<div style="
    position: fixed;
    bottom: 10px;
    left: 10px;
    z-index: 1000;
    background: white;
    padding: 5px;
    border: 1px solid black;
    font-size: 12px;">
    Escala: 1 cm ≈ 1 km
</div>
'''
mapa.get_root().html.add_child(folium.Element(legend_html))

nome_arquivo = "xxx"
mapa.save(nome_arquivo)
webbrowser.open(nome_arquivo)
