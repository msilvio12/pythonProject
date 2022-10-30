{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNxwbWAZertmjdZtclKHSlY"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZANbTlxpg3TL",
        "outputId": "1933d5a1-273e-4d76-9905-0e958f1871f6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Proyecto no terminado, esto una prueba\n"
          ]
        }
      ],
      "source": [
        "from mimetypes import init\n",
        "\n",
        "\n",
        "class Supermecado:\n",
        "     def __init__(self, cantidad_productos=0, productos=[]):\n",
        "        self.cantidad_productos=init(0)\n",
        "        self.productos=[]\n",
        "\n",
        "\n",
        "class Administracion(Supermecado):\n",
        "    def __init__(self):\n",
        "        Administracion.__init__(self)\n",
        "\n",
        "        \t\n",
        "\n",
        "class Cliente(Supermecado):\n",
        "      def __init__(self, cantidad_productos=0, productos=[]):\n",
        "          super().__init__(cantidad_productos, productos)\n",
        "          self.id=id\n",
        "          self.nombre=0\n",
        "          self.apellido=0\n",
        "          self.direccion=0\n",
        "          self.historial_compra=0\n",
        "\n",
        "class Tarjeta(Cliente):\n",
        "      def __init__(self, cantidad_productos=0, productos=[]):\n",
        "           super().__init__(cantidad_productos, productos)\n",
        "           self.id_tarj=0\n",
        "\n",
        "class Carrito(Cliente):\n",
        "      def __init__(self, cantidad_productos=0, productos=[]):\n",
        "           super().__init__(cantidad_productos, productos)\n",
        "           self.limite=30\n",
        "           self.estado_actual=0\n",
        "\n",
        "class Envios(Carrito):\n",
        "      def __init__(self, cantidad_productos=0, productos=[]):\n",
        "           super().__init__(cantidad_productos, productos)\n",
        "           self.id_envio=0\n",
        "\n",
        "\n",
        "class Productos:\n",
        "    def __init__(self, id, nombre, marca, precio, cantidad):\n",
        "        self.id=0\n",
        "        self.nombre=0\n",
        "        self.marca=0\n",
        "        self.precio=0\n",
        "        self.cantidad=0\n",
        "\n",
        "        print(Productos)\n",
        "\n",
        "\n",
        "print(\"Proyecto no terminado, esto una prueba\")        "
      ]
    }
  ]
}