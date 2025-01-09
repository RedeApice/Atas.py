# Atas das Anotações de Reuniões com os Pais

## **Descrição do Projeto**
Este projeto foi desenvolvido para extrair informações de atas de reuniões feitas pela diretoria. Ele utiliza tecnologias de OCR.

## **Funcionalidade**
- Extração de texto impresso de imagens de atas.

## **Tecnologias Utilizadas**
- **OpenCV**: Para processamento de imagens.
- **EasyOCR**: Para extração de texto (impresso ele funciona 100%).

## **Limitações**
- O OCR padrão (EasyOCR) não consegue lidar com manuscritos automaticamente, testei com o Tesseract e tive os mesmo resultados.
- A integração com GPTs personalizados exigiria a criação de APIs específicas e no caso o Aurelius-HTR não possui uma API aberta.

## **Fluxo do Projeto**
1. O arquivo de imagem da ata é enviado para a pasta do código OCR.
2. O texto manuscrito é transcrito pelo modelo.

## **Como Utilizar**
1. Clone o repositório:
   ```bash
   git clone 
   cd 