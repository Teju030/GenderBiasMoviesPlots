'''
Installations:

git clone https://github.com/huggingface/neuralcoref.git
cd neuralcoref
pip install -r requirements.txt
pip install -e .
python -m spacy download en


Versions used: spacy==2.3.7
'''

# Load your usual SpaCy model (one of SpaCy English models)
from cgitb import text
import spacy
nlp = spacy.load('en_core_web_sm')
# Add neural coref to SpaCy's pipe
import neuralcoref
# neuralcoref.add_to_pipe(nlp)


def coreference_movie_plot(plot):
    coref = neuralcoref.NeuralCoref(nlp.vocab)
    nlp.add_pipe(coref, name='neuralcoref')
    doc = nlp(plot)
    # print(doc._.has_coref)
    # print(doc._.coref_clusters)
    return doc._.coref_resolved
 

text_ = """Rohit and his younger brother Amit are orphans living in Mumbai with their landlords Lily and Anthony(to whom they regard as their aunt and uncle). Rohit is an aspiring singer who works as a salesman in a car showroom, run by Malik. One day, he meets Sonia Saxena, the beautiful daughter of wealthy Mr. Saxena, Malik's friend, when he visits her to deliver the car her father brought for her birthday. Unknown to everyone, Malik is running a drug cartel with the help of two corrupt police officers.

Rohit and Sonia meet again during her birthday party on the beach. After Rohit sings for Sonia, he is invited to perform on a cruise. Rohit and Sonia become drunk during the celebrations and fall into a lifeboat that separates from the ship. Rohit rows to an island, where they are stranded for a couple of days. During this time, they continue to fight and eventually fall in love. They are rescued by Saxena, who does not approve of their love due to their class differences. Rohit is consequently fired from his job by Malik. However, Saxena makes a deal with Rohit claiming that if Rohit becomes successful, Saxena will allow him to marry Sonia because she is from an upper-class family. Determined to prove himself, Rohit and his friends attempt to procure a record deal for him. Rohit eventually becomes a locally well-known artiste and prepares to perform at a concert.

On the day of the show, while going to pick up Amit for it, Rohit witnesses the corrupt policemen and Malik shooting and killing police commissioner, who found out about their drug dealings. They discover Rohit's presence and shoot at him, wounding him before pursuing him over a bridge. Saxena is also revealed to be part of the drug cartel and orders Rohit's murder. They knock his bike off-track, causing him to fall into the Arabian Sea below. Rohit, who doesn't know how to swim, drowns and dies. The policemen are sent to search the in the sea but are unsuccessful in finding his body. Amit is traumatized by the news and becomes mute and Rohit's family and friends, including Sonia, fall into depression.

Saxena sends Sonia to stay with his brother in New Zealand to help overcome her depression. There, she meets her cousin Neeta's friend, Raj Chopra, the son of a billionaire NRI bussinessman, who, to her immense shock, strikingly resembles Rohit, though their personalities are quite different. Raj falls for Sonia but she avoids him, due to reminding her of Rohit. Upon learning her story, Raj accompanies Sonia back to India and gives her hope to keep living, before deciding to let her go, as he knows she does not love him. However, at the airport, one of the corrupt officers spots them and opens fire on Raj. After Raj and Sonia escape, Raj realizes that somebody is mistaking him for Rohit, and the two realize that Rohit was murdered.

Raj is welcomed by Rohit's family and friends. His presence brings Amit out of his shell, and Raj learns that Amit witnessed Rohit's murder and saw the culprits. The gang decides to set a trap to expose the killers, with Raj posing as Rohit to lure them out while Amit is to identify the guilty men. During this time, Raj confesses to Sonia that he loves her. Malik, Saxena, and the officers panic upon learning that "Rohit" is alive. Raj performs at a concert in tribute to Rohit, knowing his killers will come, although Malik and the officers arrive at the concert disguised. Saxena is reunited with his daughter and learns about the plan. He calls Malik and tells him who "Rohit" really is and not to fire. After the performance, Rohit reveals to the crowd details of the shooting that he learned from Amit. Before he can reveal the names of the killers, one of the officers shoots him, causing panic in the audience, although Raj is saved due to wearing a bullet-proof jacket. Saxena tries to chastise Malik, who counterpoints that Saxena is trying to conspire with Sonia to trap them all.

To catch who they believe is Rohit, the officers kidnap Sonia and threaten to kill her if he does not reveal himself. Raj arrives at the place where she is being held. He fights the corrupt police officers and beats each of them to death, saving Sonia. Malik arrives and reveals his motive for mercilessly pursuing Raj and Sonia but is fatally shot by Saxena before he can reveal his involvement. Amit upon arriving with his family recognizes Malik as one of Rohit's killers.

Raj later learns that Saxena was the man Malik called before killing Rohit through Malik's phone. On being confronted, Saxena confesses his crime to his daughter and Raj before being arrested. As Raj is about to leave with Amit, Sonia confesses that she loves him and does not want to lose her love again, as she already lost Rohit. The couple returns to New Zealand, taking everybody with them, and they get engaged with the blessings of their families."""


coref_plot = coreference_movie_plot(text_)
print(coref_plot)