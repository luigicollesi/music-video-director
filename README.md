# Music Video Director

Skill de direção e orquestração enxuta para **Agente Videomaker** (motor OpenFilm). Combina música original, letra, imagens, vídeos, efeitos e revisão audiovisual **sem criar outro editor**.

## Princípio de eficiência

**O melhor especialista é aquele que não precisa ser chamado.** A skill tenta reutilizar o projeto e as ferramentas nativas antes de consultar uma skill complementar. Ela não carrega as dez skills do Scenario automaticamente; quando há um problema específico, seleciona no máximo uma por subtarefa, com resultado reutilizável no OpenFilm.

Leia [a matriz de encaminhamento](references/routing.md) e a [auditoria de eficiência](references/efficiency-audit.md). As economias são **hipóteses técnicas**, não percentuais medidos.

## Instalação dentro da plataforma

No Agente Videomaker, abra **Skills → Add from link** e use:

```text
https://github.com/luigicollesi/music-video-director
```

Como alternativa, pelo comando nativo do motor:

```bash
openfilm skill add https://github.com/luigicollesi/music-video-director
openfilm skills
```

A instalação pelo `npx skills add` no repositório do código-fonte é diferente da biblioteca de skills da plataforma. Prefira **Skills → Add from link** para compartilhar a skill entre projetos de vídeo. Inicie uma nova sessão do agente após instalar.

## Capacidades implementadas

- Direção narrativa e roteamento seletivo de habilidades para tarefas reais.
- Inventário local com FFprobe (`scripts/inspect_media.py`), sem reconhecimento semântico das imagens.
- Validação estrutural de marcações de letra e seções (`scripts/validate_timing.py`), **sem** alinhamento automático de áudio.
- Referências de VFX, direção e revisão de qualidade.
- Testes locais da orquestração e dos scripts.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/inspect_media.py /path/to/assets --output /path/to/project/analysis/media.json
python3 scripts/validate_timing.py references/timing-example.json
```

Requisitos dos scripts: Python 3 e FFprobe para o inventário. Ferramentas complementares podem exigir dependências extras e não são instaladas por esta skill.

## Limites

A skill não gera VFX fotorealistas automaticamente, não faz alinhamento fonético automático e não garante economia de tokens ou de tempo até haver testes A/B reais. Ela não paga por serviços, faz uploads ou utiliza o Scenario MCP sem autorização.

## Próximas versões

1. Análise musical local opcional e alinhamento de letra validado.
2. Receita de composição cinematográfica reutilizável (fogo, gelo, partículas, estilhaçamento) sem recriar a timeline.
3. Inspeção de frames e métricas de desempenho com rastreamento de revisões.
4. Benchmark A/B repetível comparando esta orquestração com OpenFilm nativo.

Licença MIT. Projeto independente baseado no motor [OpenFilm](https://github.com/openfilm/openfilm).
