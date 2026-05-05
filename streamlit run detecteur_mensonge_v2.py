import streamlit as st

st.set_page_config(
    page_title="Quel détecteur êtes-vous ?",
    page_icon="",
    layout="centered"
)

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap');

  html, body, [class*="css"] {
      background-color: #080808;
      color: #e0e0e0;
      font-family: 'Inter', sans-serif;
  }
  .stApp { background-color: #080808; }
  #MainMenu, footer, header { visibility: hidden; }

  h1 {
      font-family: 'Crimson Text', serif !important;
      color: #ffffff !important;
      font-size: 2.4rem !important;
      font-weight: 600 !important;
  }

  .phase-label {
      color: #cc0000;
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 2px;
      margin-bottom: 6px;
  }
  .phase-title {
      font-family: 'Crimson Text', serif;
      font-size: 1.9rem;
      color: #ffffff;
      margin-bottom: 6px;
      line-height: 1.2;
  }
  .phase-subtitle {
      color: #666;
      font-size: 0.88rem;
      line-height: 1.6;
      margin-bottom: 28px;
  }
  .card {
      background: #111;
      border: 1px solid #222;
      border-left: 3px solid #cc0000;
      border-radius: 6px;
      padding: 20px 24px;
      margin: 12px 0;
      font-size: 0.93rem;
      line-height: 1.7;
      color: #ccc;
  }
  .card-neutral {
      background: #111;
      border: 1px solid #222;
      border-radius: 6px;
      padding: 20px 24px;
      margin: 12px 0;
      font-size: 0.93rem;
      line-height: 1.7;
      color: #ccc;
  }
  .question-text {
      font-size: 1.05rem;
      color: #e8e8e8;
      line-height: 1.6;
      margin: 20px 0 14px;
      font-weight: 500;
  }
  .science-block {
      background: #0e0e0e;
      border: 1px solid #1e1e1e;
      border-radius: 6px;
      padding: 18px 22px;
      margin: 16px 0;
      font-size: 0.87rem;
      color: #888;
      line-height: 1.7;
  }
  .science-label {
      color: #cc0000;
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      margin-bottom: 8px;
  }
  .ref {
      color: #444;
      font-size: 0.75rem;
      font-style: italic;
      margin-top: 10px;
  }
  .score-row {
      display: flex;
      gap: 12px;
      margin: 20px 0;
  }
  .score-chip {
      background: #111;
      border: 1px solid #222;
      border-radius: 4px;
      padding: 8px 16px;
      font-size: 0.82rem;
      color: #888;
  }
  .score-chip b { color: #cc0000; }
  .dialogue-speaker {
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 5px;
  }
  .dialogue-box {
      background: #141414;
      border: 1px solid #1e1e1e;
      border-radius: 6px;
      padding: 14px 18px;
      margin: 8px 0;
      font-size: 0.93rem;
      color: #d0d0d0;
      line-height: 1.6;
      font-style: italic;
  }
  .result-big {
      font-family: 'Crimson Text', serif;
      font-size: 4.5rem;
      color: #cc0000;
      line-height: 1;
      text-align: center;
  }
  .profile-card {
      background: #111;
      border: 1px solid #222;
      border-radius: 8px;
      padding: 28px;
      margin: 20px 0;
      text-align: center;
  }
  .profile-name {
      font-family: 'Crimson Text', serif;
      font-size: 2rem;
      color: #fff;
      margin: 8px 0;
  }
  .dim-row {
      display: flex;
      justify-content: space-between;
      gap: 10px;
      margin: 16px 0;
  }
  .dim-box {
      flex: 1;
      background: #0e0e0e;
      border: 1px solid #1e1e1e;
      border-radius: 6px;
      padding: 14px;
      text-align: center;
  }
  .dim-label {
      color: #555;
      font-size: 0.68rem;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 6px;
  }
  .dim-value {
      color: #cc0000;
      font-size: 1.3rem;
      font-weight: 700;
  }
  .stButton > button {
      background: #cc0000 !important;
      color: white !important;
      border: none !important;
      border-radius: 4px !important;
      font-weight: 600 !important;
      padding: 10px 24px !important;
      font-size: 0.88rem !important;
      letter-spacing: 0.3px !important;
  }
  .stButton > button:hover { background: #aa0000 !important; }
  .stRadio > div { gap: 8px !important; }
  .stRadio label {
      background: #111 !important;
      border: 1px solid #222 !important;
      border-radius: 4px !important;
      padding: 10px 16px !important;
      color: #ccc !important;
      font-size: 0.9rem !important;
      cursor: pointer !important;
  }
  hr { border: none; border-top: 1px solid #1a1a1a; margin: 24px 0; }
</style>
""", unsafe_allow_html=True)


# ── SESSION STATE ─────────────────────────────────────────────────────────────
defaults = {
    "phase": 1,
    "p1_answers": [],
    "p1_index": 0,
    "p1_score": 0,
    "p2_answers": [],
    "p2_index": 0,
    "p2_bias_count": 0,
    "p3_strategy": None,
    "p3_index": 0,
    "p3_score": 0,
    "p3_answered": False,
    "p3_choice": None,
    "radio_key": 0,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ── DATA ──────────────────────────────────────────────────────────────────────

P1_QUESTIONS = [
    {
        "q": "Lors d'un interrogatoire tendu, un suspect pleure en racontant son histoire. Quelle est votre réaction instinctive ?",
        "options": [
            "Je ressens de la compassion et je l'écoute avec empathie",
            "Je note la réaction émotionnelle mais je reste concentré sur les faits",
            "Je me demande si les larmes sont authentiques ou stratégiques",
            "Je reste neutre, l'émotion ne change rien à mon analyse",
        ],
        "scores": [0, 1, 2, 3],
        "science": "La recherche de Duran et al. (2019) montre que les individus à faible réactivité émotionnelle au repos détectent mieux le mensonge. Ce n'est pas un manque d'empathie : c'est la capacité à percevoir sans se laisser submerger. L'empathie affective non régulée tend à activer le biais de vérité.",
        "ref": "Duran et al. (2019) · Mayer & Salovey (1997)",
    },
    {
        "q": "Vous devez évaluer la crédibilité d'un témoin dont vous appréciez personnellement la personnalité. Comment procédez-vous ?",
        "options": [
            "Je lui fais naturellement plus confiance, il m'inspire de la sympathie",
            "J'essaie de mettre de côté ma sympathie mais c'est difficile",
            "Je suis conscient du biais potentiel et je fais un effort actif pour l'écarter",
            "La relation personnelle ne joue aucun rôle dans mon analyse",
        ],
        "scores": [0, 1, 2, 3],
        "science": "La relation affective avec l'interlocuteur est l'un des facteurs qui modulent le biais de vérité (Levine, 2014). Plus on apprécie quelqu'un, plus on active le truth-default. La capacité à reconnaître ce biais et à le compenser activement est une dimension clé de l'IE-ability (Petrides & Furnham, 2001).",
        "ref": "Levine (2014) · Petrides & Furnham (2001)",
    },
    {
        "q": "Un collègue vous parle d'un projet avec beaucoup d'enthousiasme et d'émotion. Plus tard, vous réalisez que certains faits étaient exagérés. Comment réagissez-vous ?",
        "options": [
            "Je suis surpris, son enthousiasme m'avait totalement convaincu",
            "Je me souviens d'avoir eu un doute mais je l'avais mis de côté",
            "Je n'étais pas complètement convaincu mais je ne voulais pas le contrarier",
            "J'avais noté les imprécisions sur le moment mais je n'ai pas réagi",
        ],
        "scores": [0, 1, 2, 3],
        "science": "Duran et al. (2020) montrent que les énoncés chargés émotionnellement bénéficient d'un préjugé favorable indépendamment de leur véracité. L'enthousiasme et l'émotion sont des vecteurs puissants de persuasion qui contournent notre vigilance analytique.",
        "ref": "Duran et al. (2020) · ten Brinke et al. (2012)",
    },
    {
        "q": "Comment décririez-vous votre façon de prendre des décisions dans des situations sociales ambiguës ?",
        "options": [
            "Je me fie principalement à mon intuition et à ce que je ressens",
            "Je mélange intuition et réflexion selon les situations",
            "Je préfère analyser avant de conclure, même si ça prend du temps",
            "J'analyse systématiquement, l'intuition seule ne me suffit jamais",
        ],
        "scores": [0, 1, 2, 3],
        "science": "Reinhard et al. (2013) montrent que le raisonnement analytique améliore la détection quand il s'agit de chercher des incohérences. Mais l'avantage n'est pas universel : ten Brinke et al. (2012) montrent que certains jugements intuitifs très rapides peuvent être plus précis que des jugements délibérés. L'IE-ability articule les deux modes.",
        "ref": "Reinhard et al. (2013) · ten Brinke et al. (2012)",
    },
]

P2_SCENARIOS = [
    {
        "context": "Un ami vous demande de l'argent pour une urgence médicale. Il semble sincèrement inquiet et vous connaissez sa famille depuis longtemps.",
        "question": "Votre premier réflexe : vous le croyez ?",
        "answer": "biais",
        "true_lie": "vrai",
        "explanation": "Dans ce scénario, votre réponse instinctive est probablement oui. La relation affective préexistante et la charge émotionnelle de la situation activent automatiquement le biais de vérité. Levine (2014) explique que nous sommes réglés par défaut sur la confiance dans nos interactions sociales proches. Ce n'est pas une erreur, c'est une adaptation.",
        "ref": "Levine (2014) · Truth-Default Theory",
    },
    {
        "context": "Lors d'un entretien d'embauche, un candidat vous regarde droit dans les yeux, parle d'une voix assurée et décrit un parcours impressionnant sans la moindre hésitation.",
        "question": "Vous êtes enclin à le croire ?",
        "answer": "biais",
        "true_lie": "ment",
        "explanation": "Le regard direct et l'assurance vocale sont deux des stéréotypes les plus répandus de la sincérité. Or Bond et DePaulo (2006) montrent qu'ils ne sont pas corrélés avec la véracité. Un menteur expérimenté sur-contrôle précisément ces canaux visibles, comme le décrivent Ekman et Friesen avec le concept de leakage.",
        "ref": "Bond & DePaulo (2006) · Ekman & Friesen",
    },
    {
        "context": "Un inconnu dans la rue vous demande votre chemin. Il semble pressé, légèrement agité, et son histoire ne tient pas complètement debout.",
        "question": "Vous pensez qu'il vous cache quelque chose ?",
        "answer": "neutre",
        "true_lie": "vrai",
        "explanation": "L'agitation et les incohérences mineures dans un récit spontané ne sont pas des indicateurs fiables de mensonge. DePaulo et al. (2003) confirment que ces indices sont faiblement corrélés avec la tromperie. Un individu sincère mais stressé peut produire exactement ce comportement.",
        "ref": "DePaulo et al. (2003) · Zuckerman et al. (1981)",
    },
    {
        "context": "Un politique affirme à la télévision, avec conviction et de nombreux détails chiffrés, que sa réforme bénéficiera à tous les citoyens.",
        "question": "Vous êtes tenté de le croire sur le moment ?",
        "answer": "biais",
        "true_lie": "ment",
        "explanation": "La densité des détails chiffrés et la conviction du locuteur activent un biais cognitif connu : nous interprétons la précision comme un gage de vérité. Or un récit construit peut être tout aussi précis qu'un récit authentique, et Duran et al. (2020) montrent que le contenu émotionnellement engageant bénéficie d'un préjugé favorable indépendant de sa véracité.",
        "ref": "Duran et al. (2020) · Levine (2014)",
    },
]

P3_SUSPECT = {
    "name": "Thomas R., 38 ans",
    "context": "Un détournement de fonds a eu lieu dans l'entreprise. Thomas avait accès aux comptes. Il nie toute implication.",
    "normal_dialogue": [
        ("Inspecteur", "Où étiez-vous le 15 mars en soirée ?"),
        ("Thomas", "Chez moi. Je me souviens, je regardais quelque chose à la télévision."),
        ("Inspecteur", "Avez-vous accédé aux systèmes de comptabilité ce soir-là ?"),
        ("Thomas", "Non, absolument pas. Je n'avais aucune raison de le faire."),
        ("Inspecteur", "Avez-vous quelque chose à ajouter ?"),
        ("Thomas", "Non. Je suis innocent et je pense que vous faites fausse route."),
    ],
    "cognitive_dialogue": [
        ("Inspecteur", "Racontez-moi votre soirée du 15 mars en commençant par la fin et en remontant vers le début."),
        ("Thomas", "Euh... j'étais au lit. Avant ça... je dînais. Avant le dîner... je travaillais depuis chez moi. Non, attendez, j'étais sorti avant. Enfin je crois."),
        ("Inspecteur", "Vous croyez ou vous en êtes sûr ?"),
        ("Thomas", "Je suis sûr que j'étais chez moi le soir. C'est juste l'ordre que... c'est difficile à reconstituer."),
        ("Inspecteur", "À quel moment précis avez-vous fermé votre ordinateur ce soir-là ?"),
        ("Thomas", "Vers... 22h ? Ou peut-être avant. Enfin, je me souviens pas exactement de l'heure."),
    ],
    "answer": "ment",
    "normal_explanation": "Avec des questions standard, Thomas fournit des réponses vagues mais cohérentes en apparence. Rien ne permet de conclure formellement. C'est le problème central de la détection classique : sans pression cognitive, les menteurs peuvent maintenir un récit plausible.",
    "cognitive_explanation": "Quand vous demandez à Thomas de raconter les événements à l'envers, son récit s'effondre. Les incohérences apparaissent, les hésitations se multiplient, il se contredit sur des détails qu'un innocent se rappellerait facilement. Vrij (2008) démontre que cette technique augmente la charge cognitive du menteur au-delà de ses capacités de contrôle.",
    "science": "Mentir mobilise simultanément plusieurs ressources exécutives : construire un récit fictif, le maintenir cohérent, surveiller sa propre présentation et anticiper les réactions de l'interlocuteur. Raconter à l'envers ajoute une contrainte supplémentaire qui dépasse les capacités du menteur. Un innocent, lui, puise dans sa mémoire épisodique réelle et n'est pas déstabilisé par l'ordre de récupération.",
    "ref": "Vrij (2008) · Hartwig & Bond (2011) · Article 2015",
}


# ── HELPERS ───────────────────────────────────────────────────────────────────
def header(label, title, subtitle=""):
    st.markdown(f"<div class='phase-label'>{label}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='phase-title'>{title}</div>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<div class='phase-subtitle'>{subtitle}</div>", unsafe_allow_html=True)

def science_block(text, ref=""):
    st.markdown(f"""
    <div class='science-block'>
        <div class='science-label'>Éclairage scientifique</div>
        <div>{text}</div>
        <div class='ref'>{ref}</div>
    </div>
    """, unsafe_allow_html=True)

def progress_bar(current, total):
    pct = int((current / total) * 100)
    st.markdown(f"""
    <div style='margin-bottom:20px;'>
        <div style='display:flex;justify-content:space-between;margin-bottom:5px;'>
            <span style='color:#555;font-size:0.75rem;text-transform:uppercase;letter-spacing:1px;'>Progression</span>
            <span style='color:#555;font-size:0.75rem;'>{current}/{total}</span>
        </div>
        <div style='background:#1a1a1a;border-radius:2px;height:3px;'>
            <div style='background:#cc0000;height:3px;border-radius:2px;width:{pct}%;'></div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── PHASE 1 : PERSONNALITÉ ────────────────────────────────────────────────────
def phase1():
    idx = st.session_state.p1_index
    total = len(P1_QUESTIONS)

    if idx >= total:
        st.session_state.phase = 2
        st.rerun()
        return

    header(
        "Phase 1 sur 3  —  Personnalité",
        "Quel est votre profil émotionnel ?",
        "Répondez instinctivement. Il n'y a pas de bonne ou mauvaise réponse — chaque choix révèle quelque chose sur votre rapport aux émotions dans un contexte de détection."
    )

    progress_bar(idx, total)

    q = P1_QUESTIONS[idx]
    st.markdown(f"<div class='question-text'>{q['q']}</div>", unsafe_allow_html=True)

    choice = st.radio(
        "",
        q["options"],
        index=None,
        key=f"p1_radio_{idx}"
    )

    if choice:
        score = q["scores"][q["options"].index(choice)]
        science_block(q["science"], q["ref"])

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Question suivante"):
            st.session_state.p1_answers.append(score)
            st.session_state.p1_score += score
            st.session_state.p1_index += 1
            st.rerun()


# ── PHASE 2 : BIAIS DE VÉRITÉ ─────────────────────────────────────────────────
def phase2():
    idx = st.session_state.p2_index
    total = len(P2_SCENARIOS)

    if idx >= total:
        st.session_state.phase = 3
        st.rerun()
        return

    header(
        "Phase 2 sur 3  —  Cognition",
        "Mesurons votre biais de vérité.",
        "Pour chaque situation, répondez instinctivement. Ne cherchez pas la bonne réponse, cherchez votre réaction première."
    )

    progress_bar(idx, total)

    s = P2_SCENARIOS[idx]

    st.markdown(f"<div class='card'>{s['context']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='question-text'>{s['question']}</div>", unsafe_allow_html=True)

    choice = st.radio(
        "",
        ["Oui, plutôt", "Non, pas vraiment", "Je ne sais pas"],
        index=None,
        key=f"p2_radio_{idx}"
    )

    if choice:
        is_biased = (choice == "Oui, plutôt" and s["answer"] == "biais")
        if is_biased:
            st.session_state.p2_bias_count += 1

        science_block(s["explanation"], s["ref"])

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Scénario suivant"):
            st.session_state.p2_answers.append(choice)
            st.session_state.p2_index += 1
            st.rerun()


# ── PHASE 3 : CHARGE COGNITIVE ────────────────────────────────────────────────
def phase3():
    s = P3_SUSPECT

    if not st.session_state.p3_strategy:
        header(
            "Phase 3 sur 3  —  Intelligence émotionnelle en action",
            "Vous menez l'interrogatoire.",
            "Vous avez le choix de votre stratégie d'interrogatoire. Ce choix va déterminer ce que vous obtenez."
        )

        st.markdown(f"""
        <div class='card'>
            <div style='color:#cc0000;font-size:0.75rem;font-weight:700;text-transform:uppercase;
                        letter-spacing:1px;margin-bottom:10px;'>Le suspect</div>
            <b style='color:#fff;font-size:1rem;'>{s["name"]}</b><br><br>
            {s["context"]}
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='question-text'>Quelle stratégie d'interrogatoire choisissez-vous ?</div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class='card-neutral' style='min-height:120px;'>
                <div style='color:#888;font-size:0.8rem;font-weight:600;text-transform:uppercase;
                            letter-spacing:1px;margin-bottom:8px;'>Stratégie standard</div>
                Vous posez des questions directes et classiques sur les faits, l'alibi, les accès aux systèmes.
            </div>
            """, unsafe_allow_html=True)
            if st.button("Choisir cette stratégie", key="normal"):
                st.session_state.p3_strategy = "normal"
                st.rerun()
        with col2:
            st.markdown("""
            <div class='card-neutral' style='border-color:#330000;min-height:120px;'>
                <div style='color:#cc0000;font-size:0.8rem;font-weight:600;text-transform:uppercase;
                            letter-spacing:1px;margin-bottom:8px;'>Stratégie à charge cognitive</div>
                Vous demandez au suspect de raconter les événements à l'envers, posez des questions inattendues sur des détails précis.
            </div>
            """, unsafe_allow_html=True)
            if st.button("Choisir cette stratégie", key="cognitive"):
                st.session_state.p3_strategy = "cognitive"
                st.rerun()

        st.markdown("""
        <div class='science-block' style='margin-top:20px;'>
            <div class='science-label'>Pourquoi ce choix compte</div>
            Vrij (2008) démontre que les techniques à haute charge cognitive font émerger des différences comportementales
            significatives entre les menteurs et les personnes sincères. Les menteurs, contrairement aux individus honnêtes,
            n'ont pas de mémoire épisodique réelle sur laquelle s'appuyer.
            <div class='ref'>Vrij (2008) · Hartwig & Bond (2011)</div>
        </div>
        """, unsafe_allow_html=True)
        return

    strategy = st.session_state.p3_strategy
    dialogue = s["normal_dialogue"] if strategy == "normal" else s["cognitive_dialogue"]

    header(
        "Phase 3 sur 3  —  Intelligence émotionnelle en action",
        "Transcription de l'interrogatoire",
    )

    strat_label = "Stratégie standard" if strategy == "normal" else "Stratégie à charge cognitive"
    st.markdown(f"<div style='color:#555;font-size:0.8rem;margin-bottom:16px;'>Stratégie choisie : <b style='color:#888;'>{strat_label}</b></div>", unsafe_allow_html=True)

    for speaker, line in dialogue:
        color = "#cc0000" if speaker == "Inspecteur" else "#888"
        st.markdown(f"""
        <div class='dialogue-box'>
            <div class='dialogue-speaker' style='color:{color};'>{speaker.upper()}</div>
            {line}
        </div>
        """, unsafe_allow_html=True)

    if not st.session_state.p3_answered:
        st.markdown("<div class='question-text' style='margin-top:24px;'>Après cet interrogatoire, votre verdict :</div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Il dit la vérité", use_container_width=True):
                st.session_state.p3_choice = "vrai"
                st.session_state.p3_answered = True
                st.rerun()
        with col2:
            if st.button("Il ment", use_container_width=True):
                st.session_state.p3_choice = "ment"
                st.session_state.p3_answered = True
                if "ment" == s["answer"]:
                    st.session_state.p3_score = 1
                st.rerun()
    else:
        correct = st.session_state.p3_choice == s["answer"]
        explanation = s["cognitive_explanation"] if strategy == "cognitive" else s["normal_explanation"]

        bg = "#0d1a0d" if correct else "#1a0d0d"
        border = "#2d5a2d" if correct else "#5a1a1a"
        verdict_text = "Bonne détection." if correct else "Verdict incorrect."

        st.markdown(f"""
        <div style='background:{bg};border:1px solid {border};border-radius:6px;
                    padding:16px 20px;margin:16px 0;'>
            <div style='font-weight:600;color:#fff;margin-bottom:6px;'>{verdict_text}</div>
            <div style='color:#aaa;font-size:0.9rem;'>Thomas ment. Son récit ne s'appuie sur aucune mémoire épisodique réelle.</div>
        </div>
        """, unsafe_allow_html=True)

        science_block(explanation + "\n\n" + s["science"], s["ref"])

        if strategy == "normal":
            st.markdown("""
            <div style='background:#1a1000;border:1px solid #3a2800;border-radius:6px;
                        padding:14px 18px;margin:12px 0;font-size:0.88rem;color:#ccc;'>
                <b style='color:#cc8800;'>Et avec la stratégie à charge cognitive ?</b><br>
                Si vous aviez demandé à Thomas de raconter sa soirée à l'envers, les incohérences auraient été
                immédiatement visibles. La mémoire d'un menteur s'effondre sous la pression d'une récupération non linéaire.
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Voir mon profil complet"):
            st.session_state.phase = 4
            st.rerun()


# ── PHASE 4 : RÉSULTATS ───────────────────────────────────────────────────────
def phase4():
    p1 = st.session_state.p1_score
    p1_max = len(P1_QUESTIONS) * 3
    p1_pct = p1 / p1_max

    p2_bias = st.session_state.p2_bias_count
    p2_total = len(P2_SCENARIOS)
    p2_resistance = 1 - (p2_bias / p2_total)

    p3_strategy = st.session_state.p3_strategy
    p3_correct = st.session_state.p3_score == 1

    global_score = (p1_pct + p2_resistance + (1 if p3_correct else 0.5)) / 3

    if global_score >= 0.8:
        profile = "Le Détecteur Calibré"
        desc = "Vous combinez détachement émotionnel, résistance au biais de vérité et stratégie cognitive efficace. Ce profil correspond à ce que la recherche identifie comme les meilleurs détecteurs : non pas des individus insensibles, mais des individus qui régulent activement leur réactivité émotionnelle pour préserver leur lucidité analytique."
    elif global_score >= 0.6:
        profile = "L'Analyste Partiel"
        desc = "Vous avez de bonnes bases analytiques mais certains biais émotionnels influencent encore vos jugements. Votre profil d'intelligence émotionnelle est développé, mais la régulation sous pression reste un axe de progression. La distinction entre IE-trait et IE-ability de Petrides et Furnham (2001) s'applique ici : vous vous percevez comme rationnel, mais votre performance réelle est encore modulée par vos réactions affectives."
    elif global_score >= 0.4:
        profile = "La Victime du Biais de Vérité"
        desc = "Votre tendance à croire par défaut domine votre profil. C'est parfaitement adaptatif dans la vie quotidienne, comme le montre Levine (2014) avec sa Truth-Default Theory. Mais dans un contexte de détection, ce réglage par défaut vous coûte cher. Votre première piste d'amélioration serait de travailler la résistance au biais de vérité et le raisonnement analytique délibéré."
    else:
        profile = "L'Intuitif Émotionnel"
        desc = "Votre jugement est fortement guidé par vos réactions affectives immédiates. Vous avez probablement une IE-trait élevée, c'est-à-dire que vous vous percevez comme émotionnellement intelligent, mais votre IE-ability dans des tâches de détection reste limitée par une régulation insuffisante. Les travaux de Duran et al. (2019) suggèrent que le détachement émotionnel, bien plus que la sensibilité, prédit la performance en détection."

    st.markdown(f"""
    <div style='text-align:center;padding:16px 0 8px;'>
        <div style='color:#cc0000;font-size:0.7rem;font-weight:700;text-transform:uppercase;
                    letter-spacing:2px;margin-bottom:10px;'>Votre profil de détecteur</div>
        <div class='profile-name' style='font-family:Crimson Text,serif;font-size:2.2rem;color:#fff;'>{profile}</div>
    </div>
    """, unsafe_allow_html=True)

    p1_label = "Élevé" if p1_pct >= 0.67 else ("Modéré" if p1_pct >= 0.33 else "Faible")
    p2_label = "Élevée" if p2_resistance >= 0.67 else ("Modérée" if p2_resistance >= 0.33 else "Faible")
    p3_label = "Cognitive" if p3_strategy == "cognitive" else "Standard"

    st.markdown(f"""
    <div class='dim-row'>
        <div class='dim-box'>
            <div class='dim-label'>Détachement émotionnel</div>
            <div class='dim-value'>{p1_label}</div>
        </div>
        <div class='dim-box'>
            <div class='dim-label'>Résistance au biais de vérité</div>
            <div class='dim-value'>{p2_label}</div>
        </div>
        <div class='dim-box'>
            <div class='dim-label'>Stratégie d'interrogatoire</div>
            <div class='dim-value'>{p3_label}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class='card-neutral' style='margin:20px 0;'>
        <div style='color:#cc0000;font-size:0.72rem;font-weight:700;text-transform:uppercase;
                    letter-spacing:1px;margin-bottom:12px;'>Analyse de votre profil</div>
        <div style='color:#ccc;font-size:0.92rem;line-height:1.75;'>{desc}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='science-block'>
        <div class='science-label'>Ce que la recherche retient</div>
        <div style='color:#ccc;line-height:1.8;'>
        La capacité à détecter le mensonge n'est pas une compétence unitaire. C'est un profil multidimensionnel qui articule
        trois niveaux interdépendants : le détachement émotionnel comme substrat de personnalité, l'intelligence émotionnelle
        comme capacité intégratrice, et la flexibilité cognitive comme outil d'analyse. Ces dimensions interagissent : un individu
        cognitivement flexible mais émotionnellement réactif sera pénalisé par ses propres biais affectifs, tandis qu'un individu
        détaché mais rigide ne saura pas intégrer des informations contradictoires.
        </div>
        <div class='ref'>Bond & DePaulo (2006) · Duran et al. (2019) · Levine (2014) · Vrij (2008) · Mayer & Salovey (1997)</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Recommencer"):
        for k, v in defaults.items():
            st.session_state[k] = v
        st.rerun()


# ── HEADER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style='text-align:center;padding:24px 0 16px;'>
    <div style='color:#cc0000;font-size:0.68rem;font-weight:700;text-transform:uppercase;
                letter-spacing:3px;margin-bottom:10px;'>Dhaoui Nour</div>
    <h1 style='margin:0;'>Quel détecteur êtes-vous ?</h1>
    <div style='color:#444;font-size:0.85rem;margin-top:10px;font-style:italic;'>
        Trois phases pour mesurer votre personnalité, vos biais cognitifs et votre intelligence émotionnelle.
    </div>
</div>
<hr>
""", unsafe_allow_html=True)

# ── ROUTER ────────────────────────────────────────────────────────────────────
phase = st.session_state.phase
if phase == 1:
    phase1()
elif phase == 2:
    phase2()
elif phase == 3:
    phase3()
elif phase == 4:
    phase4()
