.. header:: Ambientes de Desenvolvimento Colaborativo / cTeSP em Sistemas e Tecnologias de Informação / Universidade do Algarve
.. sectnum::

============================
Tutorial de reStructuredText
============================

.. contents::

Introdução
==========

reStructuredText é útil para:
  - documentação de programas em linha (como docstrings do Python) - ver por exemplo o código em  `statemachine.py <https://docutils.sourceforge.io/docutils/statemachine.py>`_
  - para criar páginas da web simples rapidamente
  - para documentos autónomos como sejam páginas em wikis

Vejamos como estruturar um documento

Listas
======

Existem 2 tipos de listas (itemizadas/marcadores ou numeradas).


Listas - itemizadas
-------------------

Listas com marcadores:

    - Este é o item 1

    - Este é o item 2

    - ...

Notas:

    - Os marcadores são "-", "*" ou "+".
        + Podendo haver vários níveis

    - Uma linha em branco é necessária antes do primeiro item e depois do último, mas é opcional entre os itens.


Listas - enumeradas
-------------------

Nas listas numeradas podemos usar vários tipos de "enumeradores" (1, A, a, i, I) e usar vários carateres de marcação (".", ")", "()"). Exemplos:

Númeração árabe

    1. Este é o item 1

    2. Este é o item 2

Enúmeração  com letras (minúsculas)

    a) Este é o item 1

    b) Este é o item 2.

Enúmeração  com letras (mai+usculas)

    A) Este é o item 1

    B) Este é o item 2

Númeração romana (minúsculas)

    (i) Este é o item 1

    (ii) Este é o item 2

Númeração romana (maísculas)

    (I) Este é o item 1

    (II) Este é o item 2


Podemos ter vários níveis de numeração. E.g.,


    (1) Este é o item 1

        (a) subnível

            (i) subsubnível


Marcação "inline"
=================

A marcação embutida permite que palavras e frases dentro do texto tenham estilos de caracteres (como itálico e negrito) e funcionalidade (como hiperlinks).

    - *ênfase - Normalmente representado como itálico*.

    - **forte ênfase - Normalmente representado como negrito.**

    - `texto interpretado` - A renderização e o significado do texto interpretado depende do domínio ou do aplicativo. Ele pode ser usado para coisas como entradas de índice ou marcação descritiva explícita (como identificadores de programa).

    - ``literal inline`` - Normalmente processado como texto monoespaçado. Os espaços devem ser preservados, mas as quebras de linha não.

    - reference_ - Uma referência de hiperlink simples de uma palavra (ver a referência em baixo).

    - `referência de frase`_ - referência de frase, i.e., uma referência de hiperlink com espaços ou pontuação (ver a referência em baixo).

    - |referência de substituição| - O resultado é substituído na definição de substituição. Pode ser um texto, uma imagem, um hiperlink ou uma combinação destes e outros.

    - referência de nota de rodapé [1]_  - Ver notas de rodapé.

    - referência de citação [GH2017]_  - referência de citação [GH2017]

    - http://docutils.sf.net/ http://docutils.sf.net/ - Um hiperlink que será mostrado como tal.

    - `Universidade do Algarve <http://www.ualg.pt>`_


Código
======

Para incluir um bloco de código termine o parágrafo anterior com "::". O bloco pré-formatado é concluído quando o texto volta ao mesmo nível de recuo de um parágrafo anterior ao bloco pré-formatado. Por exemplo::

    from random import randint

    faces = ["cara", "coroa"]
    for lancamento in range(10):
        idx = randint(0, 1)
        print(f"Lancamento {lancamento}: {faces[idx]}")



Mas também podemos especificar a linguagem de programação para uma melhor visualização

.. code:: python

    from random import randint

    faces = ["cara", "coroa"]
    for lancamento in range(10):
        idx = randint(0, 1)
        print(f"Lancamento {lancamento}: {faces[idx]}")



Estrutura
=============

Um documento em geral tem um título e possívelmente um sub-titulo. Depois, será seccionado usando capítulos, secções e subsecções.

.. code-block:: rst

    ======
    Titulo
    ======

    ---------
    Subtitulo
    ---------

    Capítulo
    ===============

    Secção
    ------

    Subsecção
    ~~~~~~~~~~~~~~~~~~~~~~

Conclusão
=========

Para aceder às especificações do reStructuredText Markup ver [rst2020]_

Referências
===========

.. [GH2017] Greenfeld, D. & Holscher, E. (2017). The RestructuredText Book Documentation.  https://readthedocs.org/projects/restructuredtext/downloads/pdf/latest/
.. [rst2020] Goodger, D. (2020). https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html

.. [1] a nota de rodapé



.. _reference: http://www.ualg.pt

.. _referência de frase:  http://www.ualg.pt

.. |referência de substituição| image:: https://www.ualg.pt/sites/default/files/theme-logos/ualg_branco.svg
                                :height: 100
                                :width: 200
                                :scale: 50
                                :alt: alternate text