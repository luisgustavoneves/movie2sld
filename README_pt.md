movie2sld
=========

Um program python simples que cria uma página html a partir de um filme, com snapshots tirados do vídeo especificado seguidos pelo texto extraído do seu **requerido** arquivo `.srt` . Ideal para criar material de revisão a partir vídeo aulas como as da  Khan Academy ou Coursera. 
O arquivo html gerado é simples e pode ser facilmente editado para remover snapshots desnecessários.

Uso
-----

Se o arquivo `.srt` tem o mesmo nome do arquivo do filme:

`movie2sld.py video_file.mp4`

se o arquivo `.srt` tem um nome diferente:

`movie2sld.py video_file.mp4 subtitle_file.stt`

Requisitos
------------

- Python 2.7
- ffmpeg ou avconv
