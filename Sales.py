import folium
import webbrowser
from folium.plugins import MarkerCluster
from folium.plugins import MeasureControl
from folium.plugins import HeatMap
from folium.plugins import Fullscreen



def gerar_lista_pontos(pontos_cameras, pontos_wifi):
    # Combina as listas de pontos
    todos_pontos = [{"tipo": "Câmera", **p} for p in pontos_cameras] + [{"tipo": "Wi-Fi", **p} for p in pontos_wifi]

    # Ordena por número
    todos_pontos_ordenados = sorted(todos_pontos, key=lambda x: x["numero"])

    # Gera a lista formatada
    lista_formatada = [
        f"{p['numero']}: {p['nome']} ({p['tipo']})" for p in todos_pontos_ordenados
    ]

    return lista_formatada

#def calcular_ponto_medio(pontos_wifi, numeros_selecionados):
    # Filtra os pontos escolhidos com base no número
#    pontos_selecionados = [p for p in pontos_wifi if p['numero'] in numeros_selecionados]

 #   if not pontos_selecionados:
  #      raise ValueError("Nenhum ponto correspondente encontrado nos números fornecidos.")

    # Calcula a média das latitudes e longitudes
   # media_lat = sum(p['coords'][0] for p in pontos_selecionados) / len(pontos_selecionados)
    #media_lon = sum(p['coords'][1] for p in pontos_selecionados) / len(pontos_selecionados)

#    return [media_lat, media_lon]


cidade_coords = [-21.34212159973358, -49.4996554971375]  # Ajuste para sua cidade

pontos_cameras = [
    {"nome": "Portal de Entrada da Cidade", "coords": [-21.33729259071908, -49.497100118757096], "numero": 1},
    {"nome": "Acesso a Rodovia do Recinto", "coords": [-21.338775357440237, -49.502500746607275], "numero": 2},
    {"nome": "Portal de Acesso do Richileu", "coords": [-21.343696841411305, -49.50849762798308], "numero": 3},
    {"nome": "Portal de Acesso do Cervinho", "coords": [-21.34518871163603, -49.497171810205714], "numero": 4},
    {"nome": "Portal de Acesso Condomínio Lagoa", "coords": [-21.342538997570234, -49.490598821514745], "numero": 5},
    {"nome": "Bairro Enseada - Cervinho", "coords": [-21.364020668710783, -49.47564840996693], "numero": 6},
    {"nome": "Curva Acesso ao Torres", "coords": [-21.37076526996547, -49.47130100069812], "numero": 7},
    {"nome": "Continuação do Acesso ao Torres", "coords": [-21.372004970151597, -49.473479265201796], "numero": 8},
]

pontos_wifi = [
    {"nome": "Paço-Municipal", "coords": [-21.341184350617652, -49.49853717348253], "numero": 1},
    {"nome": "Sebrae", "coords": [-21.339537914040182, -49.49596232906537], "numero": 2},
    {"nome": "Detran", "coords": [-21.34275487792937, -49.49874585792042], "numero": 3},
    {"nome": "DAE", "coords": [-21.34266292800328, -49.49864793223243], "numero": 4},
    {"nome": "Assistência Social", "coords": [-21.341470115796305, -49.499113632716416], "numero": 5},
    {"nome": "CRAS", "coords": [-21.341589383618388, -49.499289025276084], "numero": 6},
    {"nome": "Conselho Tutelar", "coords": [-21.34248536108326, -49.50286062608894], "numero": 7},
    {"nome": "Projeto Girassol", "coords": [-21.339097819153412, -49.49569251705961], "numero": 8},
    {"nome": "Fundo Social", "coords": [-21.342578323166784, -49.50374376989297], "numero": 9},
    {"nome": "Pronto Socorro e ESF II", "coords": [-21.33892425959064, -49.4973615058551], "numero": 10},
    {"nome": "UBS e ESF I", "coords": [-21.344297618577826, -49.49773443702663], "numero": 11},
    {"nome": "Estrategia Saúde e Família III", "coords": [-21.338093502710798, -49.49578987524122], "numero": 12},
    {"nome": "Almoxarifado", "coords": [-21.339267018881372, -49.503117807226275], "numero": 13},
    {"nome": "Casa da Agricultura", "coords": [-21.34429119385704, -49.49910063623779], "numero": 14},
    {"nome": "Creche Oswaldo Rodrigues Estrela", "coords": [-21.335970216298087, -49.50233866389577], "numero": 15},
    {"nome": "EMEI Danilo Fernandes", "coords": [-21.341389079757757, -49.495951678788494], "numero": 16},
    {"nome": "EMEF Clorinda Morano", "coords": [-21.34372409967347, -49.49939601527565], "numero": 17},
    {"nome": "Biblioteca Municipal", "coords": [-21.343622283289783, -49.499810133138034], "numero": 18},
    {"nome": "Cozinha Piloto", "coords": [-21.34101394839546, -49.500991961715755], "numero": 19},
    {"nome": "Oficina de Música", "coords": [-21.340963982537374, -49.50119044517533], "numero": 20},
    {"nome": "Praça Municipal", "coords": [-21.34254789198355, -49.50022753214421], "numero": 21},
    {"nome": "Ginásio Municipal", "coords": [-21.341151354424593, -49.49956234428193], "numero": 22},
    {"nome": "Praia Richileu - Portaria", "coords": [-21.38326987599667, -49.555426274980015], "numero": 23},
    {"nome": "Praia Torres - Portaria", "coords": [-21.408570701219475, -49.52975041269154], "numero": 24},
    {"nome": "Praia Cervinho - Portaria", "coords": [-21.361477004613807, -49.48293103498227], "numero": 25},
    {"nome": "Recinto", "coords": [-21.335118874181592, -49.50538457516515], "numero": 26},
    {"nome": "Paço até UBS", "coords": [-21.34274098459774, -49.49813580525458], "numero": 27},
    {"nome": "Paço até Pronto Socorro", "coords": [-21.340054305104147, -49.49794933966882], "numero": 28},
    # {"nome": "Recinto", "coords": [-21.335118874181592, -49.50538457516515], "numero": 29},
    # {"nome": "Recinto", "coords": [-21.335118874181592, -49.50538457516515], "numero": 30},
    # {"nome": "Recinto", "coords": [-21.335118874181592, -49.50538457516515], "numero": 31},
    # {"nome": "Cristo - Entrada Principal", "coords": [-21.33729057369, -49.49705961200879], "numero": 32},
    # {"nome": "Recinto", "coords": [-21.335118874181592, -49.50538457516515], "numero": 33},
    # {"nome": "Recinto", "coords": [-21.335118874181592, -49.50538457516515], "numero": 34},
    # {"nome": "Recinto", "coords": [-21.335118874181592, -49.50538457516515], "numero": 35},
    # {"nome": "Recinto", "coords": [-21.335118874181592, -49.50538457516515], "numero": 36},
]

mapa = folium.Map(location=cidade_coords, zoom_start=14, tiles="CartoDB positron",
                  zoom_control=True)  ##FORMA NO PRETO HIBRIDO

# mapa = folium.Map( ##USANDO SATELITE COMO PRIO
#   location=cidade_coords,
#   tiles=None  # Para usar apenas a camada personalizada
# )

folium.TileLayer(
    tiles="CartoDB positron",
    name="Mapa Padrão",
    overlay=False,
    control=True,
).add_to(mapa)

# Adicionar a camada de satélite Esri
folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Esri",
    name="Satélite",
    overlay=False,
    control=True,
).add_to(mapa)

# Adicionar controle de camadas ao mapa
folium.LayerControl(collapsed=False).add_to(mapa)

#numeros_selecionados = [1, 10]  # Altere para os números desejados
#novo_ponto = calcular_ponto_medio(pontos_wifi, numeros_selecionados)
#rint(novo_ponto)

for ponto in pontos_cameras:
    folium.Marker(
        location=ponto["coords"],
        icon=folium.Icon(color="red", icon="camera")
    ).add_to(mapa)

    folium.map.Marker(
        location=ponto["coords"],
        icon=folium.DivIcon(
            html=f"""
            <div class="numero-label" style="
                font-size: 18px;
                color: black;
                text-shadow: 1px 1px 2px white;
            "><b>{ponto['numero']}</b></div>
            """
        )
    ).add_to(mapa)

for ponto in pontos_wifi:
    folium.Marker(
        location=ponto["coords"],
        icon=folium.Icon(color="blue", icon="cloud")
    ).add_to(mapa)

    folium.map.Marker(
        location=ponto["coords"],
        icon=folium.DivIcon(
            html=f"""
            <div class="numero-label" style="
                font-size: 18px;
                color: black;
                text-shadow: 1px 1px 2px white;
            "><b>{ponto['numero']}</b></div>
            """
        )
    ).add_to(mapa)

# Adicionar JavaScript para troca de cores
js_script = """
<script>
    function updateTextColor() {
        const labels = document.querySelectorAll('.numero-label');
        const activeLayer = document.querySelector('.leaflet-control-layers-base input:checked').nextSibling.innerText;

        labels.forEach(label => {
            if (activeLayer.includes("Satélite")) {
                label.style.color = "white";
                label.style.textShadow = "1px 1px 2px black";
            } else {
                label.style.color = "black";
                label.style.textShadow = "1px 1px 2px white";
            }
        });
    }

    // Monitorar mudanças nas camadas
    document.querySelectorAll('.leaflet-control-layers-base input').forEach(input => {
        input.addEventListener('change', updateTextColor);
    });

    // Atualizar ao carregar o mapa
    updateTextColor();
</script>
"""

# Criar lista de coordenadas para o heatmap
heatmap_data = [p["coords"] for p in pontos_cameras + pontos_wifi]

# Adicionar heatmap ao mapa
HeatMap(heatmap_data, radius=15).add_to(mapa)

coordenadas_wifi = [p["coords"] for p in pontos_wifi]
folium.PolyLine(coordenadas_wifi, color="blue", weight=2.5, opacity=1).add_to(mapa)

mapa.add_child(MeasureControl())

Fullscreen().add_to(mapa)


mapa.get_root().html.add_child(folium.Element(js_script))
#lista_pontos = gerar_lista_pontos(pontos_cameras, pontos_wifi)

# Salvar e abrir o mapa
nome_arquivo = "mapa_com_lista.html"
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
    <i>27: Intermédio entre 1 e 11</i><br>
    <i>28: Intermédio entre 1 e 10</i><br>
    <i class="fa fa-camera" style="color:red"></i> Câmeras<br>
    <i class="fa fa-cloud" style="color:blue"></i> Wi-Fi<br>
</div>
'''

mapa.get_root().html.add_child(folium.Element(legend_html))
# mapa.get_root().html.add_child(folium.Element(lista_html))


nome_arquivo = "mapa_pontos_cameras_wifi.html"
mapa.save(nome_arquivo)
webbrowser.open(nome_arquivo)