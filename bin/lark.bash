#!/bin/bash

case "$1" in
  add)
    shift
    for path in "$@"; do
      if [ -d "$path" ]; then
        # Añadir al PYTHONPATH sin duplicados
        case ":$PYTHONPATH:" in
          *":$path:"*) ;;
          *) export PYTHONPATH="${PYTHONPATH:+$PYTHONPATH:}$path" ;;
        esac
        echo "Added '$path' into PYTHONPATH"
      else
        echo "This path don't exists: $path"
      fi
    done
    ;;

  show)
    echo "PYTHONPATH actual:"
    echo "$PYTHONPATH"
    ;;

  *)
    echo "Commands:"
    echo "-  lark add <carpeta1> [carpeta2 ...]  # Añade rutas a PYTHONPATH"
    echo "-  lark show                            # Muestra PYTHONPATH actual"
    ;;
esac