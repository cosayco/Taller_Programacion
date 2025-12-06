import socket
import argparse
import json
import sys
from datetime import datetime

SERVICIOS_COMUNES = {
    20: "FTP-data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP-server",
    68: "DHCP-client",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    143: "IMAP",
    161: "SNMP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    587: "SMTP-Submission",
    636: "LDAPS",
    993: "IMAPS",
    995: "POP3S",
    1433: "MSSQL",
    1521: "Oracle",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt"
}

def cargar_servicios(custom_path: str | None):
    if custom_path:
        try:
            with open(custom_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            # Merge con mapa por defecto
            merged = {**SERVICIOS_COMUNES, **{int(k): v for k, v in data.items()}}
            return merged
        except Exception as e:
            print(f"[!] No se pudo cargar services_map.json: {e}")
    return SERVICIOS_COMUNES

def escanear_puertos(host: str, inicio: int, fin: int, timeout: float = 0.5):
    abiertos = []
    for puerto in range(inicio, fin + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        resultado = s.connect_ex((host, puerto))
        if resultado == 0:
            abiertos.append(puerto)
        s.close()
    return abiertos

def resolver_banner(host: str, puerto: int, timeout: float = 1.0):
    """Intento simple de banner grabbing (no intrusivo)."""
    try:
        with socket.create_connection((host, puerto), timeout=timeout) as s:
            s.settimeout(timeout)
            # En puertos HTTP/HTTPS/Alt intentamos una petición simple
            if puerto in (80, 8080, 8000, 8443):
                s.sendall(b"HEAD / HTTP/1.0\r\nHost: test\r\n\r\n")
                data = s.recv(256)
                return data.decode(errors="ignore").splitlines()[0][:200]
            # Para otros puertos, intentamos leer un banner si el servicio lo publica
            s.sendall(b"\r\n")
            data = s.recv(256)
            if data:
                return data.decode(errors="ignore")[:200]
    except Exception:
        pass
    return ""

def generar_recomendaciones(puertos: list[int], servicios: dict[int, str]):
    recomendaciones = []
    criticos = {22, 23, 3389, 445, 5900}
    web = {80, 8080, 8443, 443}
    bases = {3306, 5432, 1433}

    if any(p in puertos for p in criticos):
        recomendaciones.append("Revisar controles de acceso y endurecimiento (SSH/RDP/SMB/Telnet).")
    if any(p in puertos for p in web):
        recomendaciones.append("Aplicar parches, HTTPS, headers de seguridad y revisión de exposición pública en servicios web.")
    if any(p in puertos for p in bases):
        recomendaciones.append("Validar autenticación fuerte, cifrado en tránsito y restricciones de red en bases de datos.")
    if 21 in puertos or 23 in puertos:
        recomendaciones.append("Evitar protocolos inseguros (FTP/Telnet) o restringirlos a redes internas.")
    if not recomendaciones:
        recomendaciones.append("Buen estado general. Mantener inventario de servicios y escaneo periódico.")
    return recomendaciones

def formatear_reporte(host: str, rango: tuple[int, int], resultados: list[dict], recomendaciones: list[str], inicio_ts: datetime, fin_ts: datetime):
    lines = []
    lines.append("=== Auditor de red básico (Python) ===")
    lines.append(f"Host objetivo: {host}")
    lines.append(f"Rango de puertos: {rango[0]}-{rango[1]}")
    lines.append(f"Inicio: {inicio_ts.isoformat(timespec='seconds')}")
    lines.append(f"Fin:    {fin_ts.isoformat(timespec='seconds')}")
    lines.append("")
    lines.append("Puertos abiertos:")
    if resultados:
        for r in resultados:
            banner_txt = f" | Banner: {r['banner']}" if r['banner'] else ""
            lines.append(f" - {r['puerto']} ({r['servicio']}){banner_txt}")
    else:
        lines.append(" - Ninguno detectado")
    lines.append("")
    lines.append("Recomendaciones:")
    for rec in recomendaciones:
        lines.append(f" - {rec}")
    lines.append("")
    lines.append("Nota: Ejecutar solo con autorización, en laboratorio o entornos controlados.")
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(
        description="Auditor de red básico: escaneo de puertos TCP y reporte."
    )
    parser.add_argument("host", help="IP o nombre de host a auditar (laboratorio)")
    parser.add_argument("-s", "--start", type=int, default=20, help="Puerto inicial (por defecto 20)")
    parser.add_argument("-e", "--end", type=int, default=1024, help="Puerto final (por defecto 1024)")
    parser.add_argument("-t", "--timeout", type=float, default=0.5, help="Timeout por puerto (segundos)")
    parser.add_argument("--services", help="Ruta a JSON con mapa de servicios personalizado")
    parser.add_argument("-o", "--output", help="Ruta de salida del reporte (txt). Si no se indica, imprime en pantalla.")
    args = parser.parse_args()

    try:
        socket.gethostbyname(args.host)
    except socket.gaierror:
        print(f"[!] No se puede resolver el host: {args.host}")
        sys.exit(1)

    servicios = cargar_servicios(args.services)
    inicio_ts = datetime.now()
    abiertos = escanear_puertos(args.host, args.start, args.end, timeout=args.timeout)

    resultados = []
    for p in abiertos:
        servicio = servicios.get(p, "Desconocido")
        banner = resolver_banner(args.host, p)
        resultados.append({"puerto": p, "servicio": servicio, "banner": banner})

    recomendaciones = generar_recomendaciones(abiertos, servicios)
    fin_ts = datetime.now()
    reporte = formatear_reporte(args.host, (args.start, args.end), resultados, recomendaciones, inicio_ts, fin_ts)

    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(reporte)
            print(f"✅ Reporte guardado en: {args.output}")
        except Exception as e:
            print(f"[!] No se pudo escribir el reporte: {e}")
            print("----")
            print(reporte)
    else:
        print(reporte)

if __name__ == "__main__":
    main()