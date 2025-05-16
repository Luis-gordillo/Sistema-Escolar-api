# sistema_escolar_api/views/events.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sistema_escolar_api.models import Evento
from sistema_escolar_api.serializers import EventoSerializer
from django.shortcuts import get_object_or_404
from django.db import transaction
from rest_framework import generics, permissions, status

class EventoView(APIView):
    # Para restringir el acceso, puedes descomentar la siguiente línea:
    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """
        Si se pasa el parámetro "id", se retorna el evento específico;
        si no, se devuelve la lista completa de eventos.
        """
        event_id = request.GET.get("id")
        if event_id:
            evento = get_object_or_404(Evento, id=event_id)
            serializer = EventoSerializer(evento, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            eventos = Evento.objects.all().order_by("id")
            serializer = EventoSerializer(eventos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        """
        Crea un nuevo evento. Se espera que el payload tenga los siguientes campos:
          - nombre: (string)
          - tipo: (string) Ej: "Conferencia", "Taller", etc.
          - fecha_realizacion: (string) en formato "YYYY-MM-DD"
          - horaInicio: (string) formateado en 24h (ej: "00:00" o "13:00")
          - horaFin: (string) en 24h
          - lugar: (string)
          - descripcion: (string)
          - cupoAsistentes: (integer)
          - programaEducativo: (string)
          - publico_objetivo: (string) Se recomienda enviar un string, por ejemplo "Estudiantes,Profesores"
          - responsable: (string) (por ahora, dada la definición del modelo, se almacena como cadena)
        """
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventoViewEdit(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    @transaction.atomic
    def put(self, request, *args, **kwargs):
        # Se asume que en el payload viene el "id" del evento
        evento = get_object_or_404(Evento, id=request.data["id"])
        
        # Actualizar los campos del evento con los valores enviados
        evento.nombre = request.data.get("nombre", evento.nombre)
        evento.tipo = request.data.get("tipo", evento.tipo)
        evento.fecha_realizacion = request.data.get("fecha_realizacion", evento.fecha_realizacion)
        evento.horaInicio = request.data.get("horaInicio", evento.horaInicio)
        evento.horaFin = request.data.get("horaFin", evento.horaFin)
        evento.lugar = request.data.get("lugar", evento.lugar)
        evento.descripcion = request.data.get("descripcion", evento.descripcion)
        evento.cupoAsistentes = request.data.get("cupoAsistentes", evento.cupoAsistentes)
        evento.programaEducativo = request.data.get("programaEducativo", evento.programaEducativo)
        evento.publico_objetivo = request.data.get("publico_objetivo", evento.publico_objetivo)
        evento.responsable = request.data.get("responsable", evento.responsable)
        
        evento.save()
        
        serializer = EventoSerializer(evento, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)