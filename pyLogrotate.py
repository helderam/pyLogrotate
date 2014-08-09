# -*- coding: utf-8 -*-
"""
  ----------------------------------------------------------------------
  |  logrotate.py
  |  ------------
  |
  |  Programa para rodar os arquivos de log diariamente
  |  Analisa todos diretorios e arquivos com extenção .log
  |  Manter ultimos 10 arquivos, renomeando para .ant
  |  Exemplo: teste.log.1.ant
  | 
  |  :copyright: © 2014 By Helder A. Morais
  |  :license: BSD, see LICENSE for more details.
  |
  ----------------------------------------------------------------------
"""

import fnmatch
import os

# Obtem todos diretorios, subdiretorios e arquivos de .log
for root, dirs, files in os.walk('/Temp'):

	# Para cada arquivo .log encontrado
 	for filename in fnmatch.filter(files, '*.log'):

 		# Junta diretorio e nome do arquivo
 		caminho = os.path.join(root,filename)

 		# Apaga ultimo arquivo (numero 9)
		if os.path.isfile(caminho+'.9.ant'):
			os.remove(caminho+'.9.ant')

		# Renomeia outros arquivos, liberando espaço para o 1.ant	
		if os.path.isfile(caminho+'.8.ant'):
			os.rename(caminho+'.8.ant',caminho+'.9.ant')
		if os.path.isfile(caminho+'.7.ant'):
 			os.rename(caminho+'.7.ant',caminho+'.8.ant')
		if os.path.isfile(caminho+'.6.ant'):
			os.rename(caminho+'.6.ant',caminho+'.7.ant')
		if os.path.isfile(caminho+'.5.ant'):
			os.rename(caminho+'.5.ant',caminho+'.6.ant')
		if os.path.isfile(caminho+'.4.ant'):
			os.rename(caminho+'.4.ant',caminho+'.5.ant')
		if os.path.isfile(caminho+'.3.ant'):
			os.rename(caminho+'.3.ant',caminho+'.4.ant')
		if os.path.isfile(caminho+'.2.ant'):
			os.rename(caminho+'.2.ant',caminho+'.3.ant')
		if os.path.isfile(caminho+'.1.ant'):
			os.rename(caminho+'.1.ant',caminho+'.2.ant')

		# Renomeia arquivo de log para 1.ant	
		os.rename(caminho, caminho+'.1.ant')
