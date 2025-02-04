from PIL import Image

def cortar_imagem_por_altura(imagem_path, num_partes):
    imagem = Image.open(imagem_path)
    
    largura, altura = imagem.size
    
    altura_parte = altura // num_partes
    
    partes_imagem = []
    
    for i in range(num_partes):
        topo = i * altura_parte
        if i == num_partes - 1: 
            fundo = altura
        else:
            fundo = topo + altura_parte
        
        parte = imagem.crop((0, topo, largura, fundo))
        partes_imagem.append(parte)
    
    return partes_imagem

imagem_path = 'icon_types.png'
partes = cortar_imagem_por_altura(imagem_path, 19)

for i, parte in enumerate(partes):
    parte.save(f'parte_{i+1}.png')
