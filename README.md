# Atas das Anotações de Reuniões com os Pais

## **Descrição do Projeto**
Este projeto foi desenvolvido para extrair informações de atas de reuniões feitas pela diretoria. Ele utiliza tecnologias de OCR para converter imagens de texto impresso em texto editável.

## **Funcionalidade**
- Extração de texto impresso de imagens de atas utilizando tecnologias de OCR.

## **Tecnologias Utilizadas**
- **OpenCV**: Utilizado para processamento de imagens, incluindo conversão para escala de cinza, o que prepara as imagens para uma melhor análise pelo OCR.
- **Tesseract OCR**: Utilizado para a extração efetiva do texto das imagens. Prova ser uma solução robusta para reconhecimento de caracteres impressos.
- **EasyOCR**: Inicialmente utilizado para a extração de texto impresso, mostrando alto desempenho sob condições ideais.

## **Limitações**
- Ambos EasyOCR e Tesseract OCR apresentaram limitações significativas no reconhecimento de texto manuscrito, com sucessos nulos nas tentativas de transcrição automática desse tipo de escrita.
- A integração com GPTs personalizados ou sistemas de reconhecimento de texto manuscrito avançados como Aurelius-HTR exigiria desenvolvimento adicional e a criação de APIs específicas.

## **Fluxo do Projeto**
1. O arquivo de imagem da ata é carregado no diretório especificado.
2. O script processa a imagem, convertendo-a para escala de cinza.
3. O Tesseract OCR é utilizado para extrair o texto da imagem processada.
4. O texto extraído é então disponibilizado para revisão ou armazenamento (Sem sucesso).

## **Como Utilizar**
Para utilizar o projeto, siga os passos abaixo:
1. Clone o repositório:
   ```bash
   git clone
   cd
