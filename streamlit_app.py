import streamlit as st

st.title("Sciences Cognitives & Criminologie")

import streamlit as st

# ── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Détecteur de Mensonge",
    page_icon="🔍",
    layout="centered"
)

# ── CUSTOM CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;600&display=swap');

  /* Global */
  html, body, [class*="css"] {
      background-color: #0a0a0a;
      color: #e8e8e8;
      font-family: 'Inter', sans-serif;
  }
  .stApp { background-color: #0a0a0a; }

  /* Hide default streamlit elements */
  #MainMenu, footer, header { visibility: hidden; }

  /* Titles */
  h1 { font-family: 'Crimson Text', serif !important; color: #ffffff !important; font-size: 2.6rem !important; }
  h2 { font-family: 'Crimson Text', serif !important; color: #cc0000 !important; }
  h3 { color: #ffffff !important; font-size: 1.1rem !important; font-weight: 600 !important; }

  /* Scenario card */
  .scenario-card {
      background: #141414;
      border: 1px solid #2a2a2a;
      border-left: 4px solid #cc0000;
      border-radius: 6px;
      padding: 24px 28px;
      margin: 16px 0;
      font-family: 'Inter', sans-serif;
      font-size: 0.95rem;
      line-height: 1.7;
      color: #d0d0d0;
  }

  /* Dialogue bubble */
  .dialogue {
      background: #1a1a1a;
      border: 1px solid #333;
      border-radius: 8px;
      padding: 16px 20px;
      margin: 10px 0;
      font-style: italic;
      color: #e0e0e0;
      font-size: 1rem;
  }
  .dialogue-label {
      color: #cc0000;
      font-weight: 600;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 6px;
  }

  /* Clue tags */
  .clue-tag {
      display: inline-block;
      background: #1e0000;
      border: 1px solid #cc0000;
      color: #ff6666;
      border-radius: 4px;
      padding: 3px 10px;
      font-size: 0.78rem;
      margin: 3px 3px 3px 0;
  }
  .clue-tag-grey {
      display: inline-block;
      background: #1a1a1a;
      border: 1px solid #444;
      color: #888;
      border-radius: 4px;
      padding: 3px 10px;
      font-size: 0.78rem;
      margin: 3px 3px 3px 0;
  }

  /* Verdict feedback */
  .verdict-correct {
      background: #0d1f0d;
      border: 1px solid #2d5a2d;
      border-left: 4px solid #4caf50;
      border-radius: 6px;
      padding: 20px 24px;
      margin: 16px 0;
  }
  .verdict-wrong {
      background: #1f0d0d;
      border: 1px solid #5a2d2d;
      border-left: 4px solid #cc0000;
      border-radius: 6px;
      padding: 20px 24px;
      margin: 16px 0;
  }
  .verdict-title {
      font-size: 1.2rem;
      font-weight: 700;
      margin-bottom: 8px;
  }
  .science-box {
      background: #111;
      border: 1px solid #333;
      border-radius: 6px;
      padding: 16px 20px;
      margin-top: 14px;
      font-size: 0.88rem;
      color: #aaa;
      line-height: 1.6;
  }
  .science-title {
      color: #cc0000;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 8px;
  }
  .ref-tag {
      color: #666;
      font-size: 0.75rem;
      font-style: italic;
      margin-top: 8px;
  }

  /* Score bar */
  .score-bar {
      background: #1a1a1a;
      border: 1px solid #2a2a2a;
      border-radius: 6px;
      padding: 12px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
  }

  /* Progress */
  .progress-label {
      color: #666;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 4px;
  }

  /* Buttons override */
  .stButton > button {
      background: #cc0000 !important;
      color: white !important;
      border: none !important;
      border-radius: 4px !important;
      font-weight: 600 !important;
      padding: 10px 28px !important;
      font-size: 0.9rem !important;
      transition: background 0.2s !important;
  }
  .stButton > button:hover {
      background: #aa0000 !important;
  }

  /* Result screen */
  .result-screen {
      text-align: center;
      padding: 40px 20px;
  }
  .big-score {
      font-family: 'Crimson Text', serif;
      font-size: 5rem;
      color: #cc0000;
      line-height: 1;
  }
  .profile-box {
      background: #141414;
      border: 1px solid #2a2a2a;
      border-radius: 8px;
      padding: 24px;
      margin: 20px 0;
  }
  .profile-title {
      color: #cc0000;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      margin-bottom: 10px;
  }
  .profile-name {
      font-family: 'Crimson Text', serif;
      font-size: 1.8rem;
      color: #ffffff;
      margin-bottom: 8px;
  }
  .divider { border: none; border-top: 1px solid #222; margin: 20px 0; }
</style>
""", unsafe_allow_html=True)

# ── SCENARIOS DATA ────────────────────────────────────────────────────────────
SCENARIOS = [
    {
        "id": 1,
        "title": "L'Alibi du Vendredi Soir",
        "context": "Un vol a eu lieu vendredi soir entre 21h et 23h dans un appartement du 3e arrondissement. Vous interrogez Marc, 34 ans, ancien colocataire de la victime.",
        "dialogue": [
            ("Inspecteur", "Où étiez-vous vendredi soir entre 21h et 23h ?"),
            ("Marc", "J'étais chez moi. Je regardais une série, Netflix je crois. Oui, c'était Netflix."),
            ("Inspecteur", "Vous avez regardé quoi exactement ?"),
            ("Marc", "Euh... une série policière. Je me souviens plus du nom précisément. J'en regarde tellement..."),
            ("Inspecteur", "Quelqu'un peut confirmer votre présence ?"),
            ("Marc", "Non, j'étais seul. Mais je vous jure que j'étais là. Pourquoi je mentirais ?"),
        ],
        "clues_visible": [
            "Répète 'Netflix' comme pour s'en convaincre",
            "Ne se souvient pas du nom de la série",
            "Ajoute spontanément 'Pourquoi je mentirais ?'",
        ],
        "clues_stereotype": [
            "Ne fuit pas le regard",
            "Voix stable, pas d'agitation visible",
        ],
        "answer": "ment",
        "answer_label": "Il ment",
        "explanation": "Marc présente plusieurs signaux cognitifs classiques du mensonge : il sur-spécifie puis se rétracte ('Netflix je crois… oui c'était Netflix'), échoue à fournir des détails concrets sur une activité censément normale, et utilise la formule 'Pourquoi je mentirais ?': une stratégie rhétorique typique du menteur pour détourner l'attention (DePaulo et al., 2003).\n\nNotez aussi qu'il ne fuit PAS le regard et que sa voix est stable, deux stéréotypes souvent utilisés à tort comme indices de mensonge. La recherche montre que ces signaux ne sont pas fiables (Bond & DePaulo, 2006).",
        "science_concept": "Le menteur sur-contrôle certains canaux (regard, voix) mais laisse filtrer des incohérences dans le contenu verbal — c'est le principe du 'leakage' cognitif.",
        "stereotype_trap": "Regard direct et voix stable ≠ vérité. Ces indices ne sont pas corrélés avec la tromperie.",
        "ref": "DePaulo et al. (2003) · Bond & DePaulo (2006) · Ekman & Friesen",
    },
    {
        "id": 2,
        "title": "La Collègue Absente",
        "context": "Une fraude interne a été commise dans votre entreprise. 15 000€ ont disparu des comptes. Vous interrogez Sandra, 41 ans, comptable depuis 8 ans, qui avait accès aux fichiers concernés.",
        "dialogue": [
            ("Inspecteur", "Avez-vous accédé aux fichiers de facturation le 12 mars ?"),
            ("Sandra", "Non, absolument pas. Ce jour-là j'étais en réunion toute la matinée, puis j'ai déjeuné avec Léa des RH, vous pouvez lui demander, elle confirme."),
            ("Inspecteur", "Et l'après-midi ?"),
            ("Sandra", "L'après-midi j'avais des urgences sur le bilan trimestriel. Je suis restée à mon bureau jusqu'à 19h. Plusieurs collègues m'ont vue."),
            ("Inspecteur", "Avez-vous une idée de qui aurait pu faire ça ?"),
            ("Sandra", "Honnêtement non. Mais je sais que Thomas avait des problèmes financiers récemment. Je dis ça sans l'accuser hein."),
        ],
        "clues_visible": [
            "Alibi détaillé, spontané et vérifiable",
            "Nomme des témoins précis pour chaque moment",
            "Ajoute une précision ('sans l'accuser') qui montre une conscience sociale",
        ],
        "clues_stereotype": [
            "Parle vite, semble nerveuse",
            "Joue avec son stylo pendant l'interrogatoire",
        ],
        "answer": "vrai",
        "answer_label": "Elle dit la vérité",
        "explanation": "Sandra présente un profil de véracité : elle fournit un alibi détaillé avec des témoins nommés et vérifiables, elle répond directement aux questions sans évasion, et sa mention de Thomas est accompagnée d'une modération spontanée qui indique une pensée sociale complexe, pas une stratégie de diversion.\n\nSon agitation (parle vite, joue avec un stylo) est souvent interprétée comme un signe de mensonge. C'est un stéréotype faux : le stress d'un innocent interrogé peut produire exactement ces comportements (Vrij, 2008).",
        "science_concept": "Un récit vrai est généralement riche en détails contextuels, ancrés dans la mémoire épisodique. Un récit inventé tend à être vague ou sur-simplifié.",
        "stereotype_trap": "Nervosité et agitation = stéréotype du menteur. Un innocent interrogé peut être tout aussi agité, voire plus.",
        "ref": "Vrij (2008) · Zuckerman et al. (1981) · DePaulo et al. (2003)",
    },
    {
        "id": 3,
        "title": "Le Témoin Trop Sûr",
        "context": "Un accident de voiture a eu lieu à un carrefour. Un piéton a été renversé. Vous interrogez Karim, 28 ans, qui se présente comme témoin direct de la scène.",
        "dialogue": [
            ("Inspecteur", "Décrivez-moi exactement ce que vous avez vu."),
            ("Karim", "La voiture est arrivée à toute vitesse, le feu était rouge, le conducteur n'a même pas freiné. C'est clair, net, précis."),
            ("Inspecteur", "À quelle distance étiez-vous ?"),
            ("Karim", "Pas loin. Enfin... de l'autre côté du carrefour. Mais je voyais très bien."),
            ("Inspecteur", "Le conducteur, vous pouvez le décrire ?"),
            ("Karim", "Oui. Enfin non, j'ai pas vu son visage. Mais la voiture était rouge, j'en suis certain. Ou peut-être bordeaux."),
            ("Inspecteur", "Vous avez vu la couleur du feu ?"),
            ("Karim", "Oui, rouge. Enfin, je suppose que c'était rouge. Logiquement c'était rouge sinon l'accident aurait pas eu lieu, non ?"),
        ],
        "clues_visible": [
            "Certitude initiale très forte ('clair, net, précis')",
            "Les détails se rétractent progressivement",
            "Raisonnement circulaire : déduit le feu rouge de l'accident lui-même",
        ],
        "clues_stereotype": [
            "Regard direct et assuré",
            "Ton confiant, pas d'hésitation dans la voix",
        ],
        "answer": "ment",
        "answer_label": "Il ment (ou déforme la réalité)",
        "explanation": "Karim ne ment pas forcément de manière intentionnelle, mais son témoignage est construit plutôt que mémorisé. Il commence par une certitude totale ('clair, net, précis'), puis recule sur chaque détail concret : la distance, la couleur du véhicule, la couleur du feu. Le plus révélateur : il déduit la couleur du feu à partir de la logique de l'accident, pas d'une observation réelle.\n\nCe cas illustre la différence entre un récit mémorisé (riche en détails sensoriels cohérents) et un récit reconstruit (affirmations générales + détails qui s'effondrent sous pression).",
        "science_concept": "La charge cognitive augmentée (questions précises) fait émerger les incohérences entre ce qu'on prétend avoir vu et ce qu'on a réellement mémorisé.",
        "stereotype_trap": "Confiance et assurance dans le ton ne signifient pas véracité. Parfois, les témoins les plus affirmatifs sont ceux dont le récit est le plus reconstruit.",
        "ref": "Vrij (2008) · Article 2015 · Hartwig & Bond (2011)",
    },
    {
        "id": 4,
        "title": "La Dispute du Soir",
        "context": "Une agression s'est produite dans un bar. Une femme, Inès, 26 ans, affirme avoir été victime d'une agression verbale et physique de la part d'un inconnu. Vous l'interrogez.",
        "dialogue": [
            ("Inspecteur", "Racontez-moi ce qui s'est passé."),
            ("Inès", "C'était horrible. Il est arrivé par derrière, j'ai senti son souffle dans mon cou, ça sentait l'alcool. Il a attrapé mon bras et m'a dit de me taire."),
            ("Inspecteur", "Vous pouvez le décrire ?"),
            ("Inès", "Grand, cheveux sombres, une veste grise ou non, bleu marine. Il avait une cicatrice ici... *(montre sa joue gauche)*. J'essaie de me souvenir exactement mais j'étais tellement paniquée."),
            ("Inspecteur", "Il y avait du monde autour ?"),
            ("Inès", "Oui, beaucoup de monde. Mais personne n'a réagi, c'est ça qui m'a choquée le plus, en fait."),
        ],
        "clues_visible": [
            "Détails sensoriels précis (souffle, odeur, sensation physique)",
            "Incertitude sur un détail (couleur de la veste) avec correction spontanée",
            "Émotion cohérente avec l'événement rapporté",
        ],
        "clues_stereotype": [
            "Voix qui tremble légèrement",
            "Hésite sur la couleur de la veste",
        ],
        "answer": "vrai",
        "answer_label": "Elle dit la vérité",
        "explanation": "Le témoignage d'Inès présente les marqueurs classiques d'un récit véridique : richesse des détails sensoriels (souffle, odeur d'alcool, sensation physique), cohérence émotionnelle, et surtout une auto-correction spontanée sur la couleur de la veste, un signe fort de mémoire réelle plutôt que de récit construit.\n\nLes menteurs tendent à éviter les auto-corrections de peur de paraître peu crédibles. Un vrai souvenir, lui, évolue naturellement sous la pression de la récupération mémorielle.",
        "science_concept": "Les récits vrais contiennent plus de détails sensoriels non pertinents pour la narration (odeur, texture, sensation). Les récits inventés tendent à se concentrer sur les éléments 'importants' uniquement.",
        "stereotype_trap": "La voix qui tremble et les hésitations sont interprétées comme des signes de mensonge. En réalité, elles indiquent souvent une émotion authentique ou un effort de récupération mémorielle.",
        "ref": "DePaulo et al. (2003) · Vrij et al. (2007) · Duran et al. (2020)",
    },
    {
        "id": 5,
        "title": "Le Manager Sous Pression",
        "context": "Des données confidentielles de votre entreprise ont été transmises à un concurrent. Vous interrogez David, 45 ans, directeur commercial, qui avait accès à ces données.",
        "dialogue": [
            ("Inspecteur", "Avez-vous partagé des données avec la société Nexum ?"),
            ("David", "Écoutez, je vais être très clair : je n'ai jamais, au grand jamais, transmis quoi que ce soit à qui que ce soit en dehors des procédures officielles."),
            ("Inspecteur", "Avez-vous eu des contacts avec Nexum récemment ?"),
            ("David", "Des contacts ? Dans le cadre professionnel normal, peut-être. C'est mon travail de rencontrer des gens du secteur."),
            ("Inspecteur", "Et en dehors du cadre professionnel ?"),
            ("David", "Je ne vois pas ce que vous voulez dire. Je pense que vous devriez vous concentrer sur les vrais problèmes de sécurité informatique plutôt que de m'interroger moi."),
        ],
        "clues_visible": [
            "Réponse initiale hyper formelle et suraffirmée",
            "Réinterprète 'contacts' pour élargir la définition",
            "Contre-attaque en redirigeant l'attention",
        ],
        "clues_stereotype": [
            "Regard assuré, posture droite",
            "Ton professionnel et calme",
        ],
        "answer": "ment",
        "answer_label": "Il ment",
        "explanation": "David utilise trois stratégies classiques du menteur sophistiqué. D'abord la suraffirmation : 'jamais, au grand jamais', les personnes sincères ont rarement besoin de telles formulations superlatives. Ensuite la réinterprétation sémantique : il redéfinit 'contacts' pour inclure une version anodine. Enfin la contre-attaque : il redirige l'interrogatoire pour esquiver.\n\nSon calme apparent et son regard assuré sont précisément ce qu'un menteur expérimenté produit intentionnellement, le 'sur-contrôle' du canal non verbal décrit par Ekman & Friesen.",
        "science_concept": "Les menteurs sophistiqués sur-contrôlent les canaux visibles (posture, regard) mais leur stratégie verbale révèle des patterns caractéristiques : suraffirmation, esquive sémantique, contre-attaque.",
        "stereotype_trap": "Calme et assurance = souvent interprétés comme signes de sincérité. Chez un menteur expérimenté, c'est exactement l'inverse : le calme est produit intentionnellement.",
        "ref": "Ekman & Friesen · Vrij (2008) · Meissner & Kassin (2002)",
    },
]

# ── SESSION STATE ─────────────────────────────────────────────────────────────
if "current" not in st.session_state:
    st.session_state.current = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "user_choice" not in st.session_state:
    st.session_state.user_choice = None
if "screen" not in st.session_state:
    st.session_state.screen = "game"  # "game" | "result"

# ── RESULT SCREEN ─────────────────────────────────────────────────────────────
def show_result():
    score = st.session_state.score
    total = len(SCENARIOS)
    pct = score / total

    if pct == 1.0:
        profile = "Le Wizard"
        desc = "Précision parfaite. Vous faites partie des rares individus que la recherche appelle les 'wizards' — naturellement attentifs aux signaux cognitifs réels plutôt qu'aux stéréotypes."
        emoji = "🔮"
    elif pct >= 0.8:
        profile = "L'Analyste"
        desc = "Excellent résultat. Vous résistez bien aux stéréotypes et mobilisez un raisonnement analytique efficace. Quelques biais persistent, mais votre profil est celui d'un bon détecteur."
        emoji = "🧠"
    elif pct >= 0.6:
        profile = "L'Apprenti Détective"
        desc = "Bon début. Vous détectez mieux que la moyenne (54% selon Bond & DePaulo, 2006), mais certains stéréotypes influencent encore vos jugements. La bonne science s'apprend."
        emoji = "🔍"
    elif pct >= 0.4:
        profile = "La Victime du Biais de Vérité"
        desc = "Vous avez tendance à croire les gens — c'est humain et adaptatif (Levine, 2014). Mais dans un contexte de détection, ce biais vous coûte cher. Entraînez votre scepticisme."
        emoji = "⚖️"
    else:
        profile = "L'Esclave des Stéréotypes"
        desc = "Votre jugement est fortement guidé par des indices non fiables — regard, ton, nervosité. La recherche montre que ces indices sont quasi inutiles (DePaulo et al., 2003)."
        emoji = "🪞"

    st.markdown(f"""
    <div class='result-screen'>
        <div style='color:#666;font-size:0.8rem;text-transform:uppercase;letter-spacing:2px;margin-bottom:12px;'>
            RÉSULTAT FINAL
        </div>
        <div class='big-score'>{score}/{total}</div>
        <div style='color:#888;margin:8px 0 30px;font-size:1rem;'>bonnes réponses</div>
        <div class='profile-box'>
            <div class='profile-title'>VOTRE PROFIL DE DÉTECTEUR</div>
            <div style='font-size:2.5rem;margin-bottom:8px;'>{emoji}</div>
            <div class='profile-name'>{profile}</div>
            <hr class='divider'>
            <div style='color:#aaa;font-size:0.92rem;line-height:1.7;'>{desc}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='background:#111;border:1px solid #222;border-radius:6px;padding:20px 24px;margin-top:8px;'>
        <div style='color:#cc0000;font-size:0.75rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px;'>
            CE QUE LA SCIENCE RETIENT
        </div>
        <div style='color:#888;font-size:0.88rem;line-height:1.7;'>
            • <b style='color:#ccc;'>54%</b> — la précision moyenne humaine dans la détection du mensonge (Bond & DePaulo, 2006)<br>
            • Les indices classiques (regard fuyant, agitation) sont <b style='color:#ccc;'>non fiables</b> (DePaulo et al., 2003)<br>
            • Les vrais signaux sont <b style='color:#ccc;'>cognitifs et verbaux</b> : incohérences, suraffirmation, esquive sémantique<br>
            • Le détachement émotionnel améliore la détection (Duran et al., 2019)<br>
            • Le biais de vérité nous pousse à croire par défaut — c'est adaptatif mais coûteux (Levine, 2014)
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄  Recommencer"):
        st.session_state.current = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.user_choice = None
        st.session_state.screen = "game"
        st.rerun()

# ── GAME SCREEN ───────────────────────────────────────────────────────────────
def show_game():
    idx = st.session_state.current
    s = SCENARIOS[idx]
    total = len(SCENARIOS)

    # ── Header
    st.markdown(f"""
    <div style='display:flex;justify-content:space-between;align-items:center;
                border-bottom:1px solid #1e1e1e;padding-bottom:14px;margin-bottom:20px;'>
        <div>
            <div style='color:#cc0000;font-size:0.7rem;font-weight:700;text-transform:uppercase;
                        letter-spacing:1.5px;margin-bottom:4px;'>INTERROGATOIRE {idx+1}/{total}</div>
            <div style='font-family:Crimson Text,serif;font-size:1.6rem;color:#fff;font-weight:600;'>
                {s["title"]}
            </div>
        </div>
        <div style='text-align:right;'>
            <div style='color:#666;font-size:0.7rem;text-transform:uppercase;letter-spacing:1px;'>Score</div>
            <div style='font-size:1.4rem;font-weight:700;color:#cc0000;'>{st.session_state.score}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Context
    st.markdown(f"""
    <div class='scenario-card'>
        <div style='color:#cc0000;font-size:0.72rem;font-weight:700;text-transform:uppercase;
                    letter-spacing:1px;margin-bottom:10px;'>📁 CONTEXTE</div>
        {s["context"]}
    </div>
    """, unsafe_allow_html=True)

    # ── Dialogue
    st.markdown("<div style='margin:20px 0 10px;color:#666;font-size:0.75rem;text-transform:uppercase;letter-spacing:1px;'>🎙️ TRANSCRIPTION DE L'INTERROGATOIRE</div>", unsafe_allow_html=True)
    for speaker, line in s["dialogue"]:
        color = "#cc0000" if speaker == "Inspecteur" else "#aaaaaa"
        align = "left"
        st.markdown(f"""
        <div class='dialogue'>
            <div class='dialogue-label' style='color:{color};'>{speaker.upper()}</div>
            {line}
        </div>
        """, unsafe_allow_html=True)

    # ── Clues
    st.markdown("<div style='margin:20px 0 8px;color:#666;font-size:0.75rem;text-transform:uppercase;letter-spacing:1px;'>🔎 INDICES OBSERVÉS</div>", unsafe_allow_html=True)
    clues_html = ""
    for c in s["clues_visible"]:
        clues_html += f"<span class='clue-tag'>⚠ {c}</span>"
    for c in s["clues_stereotype"]:
        clues_html += f"<span class='clue-tag-grey'>👁 {c}</span>"
    st.markdown(f"<div>{clues_html}</div>", unsafe_allow_html=True)

    st.markdown("<div style='margin:6px 0 4px;'><span style='color:#cc0000;font-size:0.75rem;'>⚠ Signal possible</span> &nbsp;&nbsp; <span style='color:#555;font-size:0.75rem;'>👁 Stéréotype courant</span></div>", unsafe_allow_html=True)

    # ── Decision
    if not st.session_state.answered:
        st.markdown("<div style='margin:28px 0 12px;color:#888;font-size:0.85rem;'>Votre verdict :</div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅  Cette personne dit la vérité", use_container_width=True):
                st.session_state.user_choice = "vrai"
                st.session_state.answered = True
                if "vrai" == s["answer"]:
                    st.session_state.score += 1
                st.rerun()
        with col2:
            if st.button("❌  Cette personne ment", use_container_width=True):
                st.session_state.user_choice = "ment"
                st.session_state.answered = True
                if "ment" == s["answer"]:
                    st.session_state.score += 1
                st.rerun()

    # ── Feedback
    else:
        correct = st.session_state.user_choice == s["answer"]
        verdict_class = "verdict-correct" if correct else "verdict-wrong"
        verdict_icon = "✅" if correct else "❌"
        verdict_text = "Bonne détection !" if correct else "Raté — votre jugement a été biaisé."

        st.markdown(f"""
        <div class='{verdict_class}'>
            <div class='verdict-title'>{verdict_icon} {verdict_text}</div>
            <div style='color:#aaa;font-size:0.9rem;margin-bottom:4px;'>
                <b style='color:#fff;'>Réponse :</b> {s["answer_label"]}
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class='science-box'>
            <div class='science-title'>🧪 EXPLICATION SCIENTIFIQUE</div>
            <div style='color:#ccc;margin-bottom:12px;white-space:pre-line;'>{s["explanation"]}</div>
            <div style='background:#0d0d0d;border:1px solid #cc0000;border-radius:4px;
                        padding:10px 14px;margin:10px 0;'>
                <div style='color:#cc0000;font-size:0.72rem;font-weight:700;
                            text-transform:uppercase;letter-spacing:1px;margin-bottom:5px;'>
                    CONCEPT CLÉ
                </div>
                <div style='color:#ddd;font-size:0.88rem;'>{s["science_concept"]}</div>
            </div>
            <div style='background:#1a0000;border-radius:4px;padding:10px 14px;margin:10px 0;'>
                <div style='color:#ff6666;font-size:0.72rem;font-weight:700;
                            text-transform:uppercase;letter-spacing:1px;margin-bottom:5px;'>
                    ⚠ PIÈGE STÉRÉOTYPE
                </div>
                <div style='color:#ccc;font-size:0.88rem;'>{s["stereotype_trap"]}</div>
            </div>
            <div class='ref-tag'>📚 {s["ref"]}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        if idx < total - 1:
            if st.button("Interrogatoire suivant →", use_container_width=True):
                st.session_state.current += 1
                st.session_state.answered = False
                st.session_state.user_choice = None
                st.rerun()
        else:
            if st.button("Voir mon profil de détecteur →", use_container_width=True):
                st.session_state.screen = "result"
                st.rerun()

# ── HEADER ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div style='text-align:center;padding:20px 0 10px;'>
    <div style='color:#cc0000;font-size:0.7rem;font-weight:700;text-transform:uppercase;
                letter-spacing:3px;margin-bottom:8px;'>DHAOUI Nour</div>
    <h1 style='margin:0;font-size:2.2rem;'>Détecteur de Mensonge</h1>
    <div style='color:#555;font-size:0.85rem;margin-top:8px;font-style:italic;'>
        Vous jouez le rôle de l'inspecteur. Chaque décision révèle vos biais.
    </div>
</div>
<hr style='border:none;border-top:1px solid #1e1e1e;margin:16px 0 24px;'>
""", unsafe_allow_html=True)

# ── ROUTER ────────────────────────────────────────────────────────────────────
if st.session_state.screen == "result":
    show_result()
else:
    show_game()
