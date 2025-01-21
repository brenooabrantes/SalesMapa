import folium
import webbrowser
from folium.plugins import FloatImage

cidade_coords = [-21.34212159973358, -49.4996554971375]  # Ajuste para sua cidade

pontos_cameras = [
    {"nome": "Portal de Entrada da Cidade", "coords": [-21.33729259071908, -49.497100118757096], "numero": 1},
    {"nome": "Acesso a Rodovia do Recinto", "coords": [-21.338775357440237, -49.502500746607275], "numero": 2},
    {"nome": "Portal de Acesso do Richileu", "coords": [-21.343696841411305, -49.50849762798308], "numero": 3},
    {"nome": "Portal de Acesso do Cervinho", "coords": [-21.34518871163603, -49.497171810205714], "numero": 4},
    {"nome": "Portal de Acesso Condomínio Lagoa", "coords": [-21.342538997570234, -49.490598821514745], "numero": 5},
    #{"nome": "Portal de Acesso do Richileu", "coords": [-21.342538997570234, -49.490598821514745], "numero": 3},
    #{"nome": "Portal de Acesso do Richileu", "coords": [-21.343696841411305, -49.50849762798308], "numero": 3},
    #{"nome": "Portal de Acesso do Richileu", "coords": [-21.343696841411305, -49.50849762798308], "numero": 3},
]

pontos_wifi = [
    {"nome": "Paço-Municipal", "coords": [-21.341184350617652, -49.49853717348253], "numero": 1},
    {"nome": "Sebrae", "coords": [-21.339537914040182, -49.49596232906537], "numero": 2},
    {"nome": "Detran", "coords": [-21.34275487792937, -49.49874585792042], "numero": 3},
    ##{"nome": "DAE", "coords": [-21.34275487792937, -49.49874585792042], "numero": 4},
    {"nome": "CRAS", "coords": [-21.341505630766136, -49.49917672763313], "numero": 5},
    #{"nome": "Detran", "coords": [-21.34275487792937, -49.49874585792042], "numero": 3},
    #{"nome": "Detran", "coords": [-21.34275487792937, -49.49874585792042], "numero": 3},
    #{"nome": "Detran", "coords": [-21.34275487792937, -49.49874585792042], "numero": 3},
    #{"nome": "Detran", "coords": [-21.34275487792937, -49.49874585792042], "numero": 3},
    #{"nome": "Detran", "coords": [-21.34275487792937, -49.49874585792042], "numero": 3},
    {"nome": "UBS e ESF I", "coords": [-21.344297618577826, -49.49773443702663], "numero": 11},
    #{"nome": "Detran", "coords": [-21.34275487792937, -49.49874585792042], "numero": 3},
    #{"nome": "Detran", "coords": [-21.341118320223273, -49.503566141915876], "numero": 13},
    {"nome": "Detran", "coords": [-21.34429119385704, -49.49910063623779], "numero": 14},
    #{"nome": "Detran", "coords": [-21.34275487792937, -49.49874585792042], "numero": 3},
    {"nome": "EMEI Danilo Fernandes", "coords": [-21.341389079757757, -49.495951678788494], "numero": 16},
    {"nome": "EMEF Clorinda Morano", "coords": [-21.34372409967347, -49.49939601527565], "numero": 17},
    {"nome": "Biblioteca Municipal", "coords": [-21.343622283289783, -49.499810133138034], "numero": 18},
    {"nome": "Cozinha Piloto", "coords": [-21.34101394839546, -49.500991961715755], "numero": 19},
    {"nome": "Oficina de Música", "coords": [-21.340963982537374, -49.50119044517533], "numero": 20},
    {"nome": "Praça Municipal", "coords": [-21.34254789198355, -49.50022753214421], "numero": 21},
    {"nome": "Ginásio Municipal", "coords": [-21.341151354424593, -49.49956234428193], "numero": 22},
    #{"nome": "Praça Municipal", "coords": [-21.34254789198355, -49.50022753214421], "numero": 21},
    #{"nome": "Praça Municipal", "coords": [-21.34254789198355, -49.50022753214421], "numero": 21},
    #{"nome": "Praça Municipal", "coords": [-21.34254789198355, -49.50022753214421], "numero": 21},
    {"nome": "Recinto", "coords": [-21.335118874181592, -49.50538457516515], "numero": 26},
    #{"nome": "Recinto", "coords": [-21.335118874181592, -49.50538457516515], "numero": 26},
    #{"nome": "Recinto", "coords": [-21.335118874181592, -49.50538457516515], "numero": 26},
    #{"nome": "Recinto", "coords": [-21.335118874181592, -49.50538457516515], "numero": 26},
    #{"nome": "Recinto", "coords": [-21.335118874181592, -49.50538457516515], "numero": 26},
    #{"nome": "Recinto", "coords": [-21.335118874181592, -49.50538457516515], "numero": 26},
    {"nome": "Cristo - Entrada Principal", "coords": [-21.33729057369, -49.49705961200879], "numero": 32},
    #{"nome": "Recinto", "coords": [-21.335118874181592, -49.50538457516515], "numero": 32},
    #{"nome": "Recinto", "coords": [-21.335118874181592, -49.50538457516515], "numero": 32},
    #{"nome": "Recinto", "coords": [-21.335118874181592, -49.50538457516515], "numero": 32},
    #{"nome": "Recinto", "coords": [-21.335118874181592, -49.50538457516515], "numero": 32},
]

#mapa = folium.Map(location=cidade_coords, zoom_start=14, tiles="CartoDB positron") ##FORMA NO PRETO HIBRIDO
#mapa = folium.Map(location=cidade_coords, zoom_start=14, tiles="Stamen Terrain", zoom_control=True)

mapa = folium.Map( ##USANDO SATELITE COMO PRIO
    location=cidade_coords,
    zoom_start=14,
    tiles=None  # Para usar apenas a camada personalizada
)

# Adicionando camada de satélite Esri
folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Esri",
    name="Esri Satellite",
    overlay=False,
    control=True,
).add_to(mapa)

for ponto in pontos_cameras:
    folium.Marker(
        location=ponto["coords"],
        icon=folium.Icon(color="red", icon="camera")  # Ícone vermelho para câmeras
    ).add_to(mapa)

    folium.map.Marker(
        location=ponto["coords"],
        icon=folium.DivIcon(
            html=f"""<div style="font-size: 18px; color: white;"><b>{ponto['numero']}</div>"""
            #html=f"""<div style="font-size: 18px; color: black;"><b>{ponto['numero']}</div>"""
        )
    ).add_to(mapa)

for ponto in pontos_wifi:
    folium.Marker(
        location=ponto["coords"],
        icon=folium.Icon(color="blue", icon="cloud")  # Ícone de Wi-Fi
    ).add_to(mapa)

    folium.map.Marker(
        location=ponto["coords"],
        icon=folium.DivIcon(
            html=f"""<div style="font-size: 18px; color: white;"><b>{ponto['numero']}</b></div>"""
            #html=f"""<div style="font-size: 18px; color: purple;"><b>{ponto['numero']}</b></div>"""
        )
    ).add_to(mapa)

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
mapa.get_root().html.add_child(folium.Element(legend_html))

nome_arquivo = "mapa_pontos_cameras_wifi.html"
mapa.save(nome_arquivo)
webbrowser.open(nome_arquivo)