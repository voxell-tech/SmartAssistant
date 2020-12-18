using System.Collections; 
using System;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using UnityEngine.Windows.Speech;

public class VoiceRecon : MonoBehaviour
{
  private KeywordRecognizer keywordRecognizer;
  [SerializeField]
  private string[] keywords;
  private Dictionary<string,Action> keywordDict; //format of dictionary
  
  void Start()
  {
    keywordDict = new Dictionary<string,Action>(); // new dictionary
    keywordDict.Add("hello", greet);

    keywordRecognizer = new KeywordRecognizer(keywordDict.Keys.ToArray());
    keywordRecognizer.OnPhraseRecognized += OnKeyWordRecognize;
    keywordRecognizer.Start();
  }

  private void OnKeyWordRecognize(PhraseRecognizedEventArgs speech)
  {
    Debug.Log("Key Word :" + speech.text);
    keywordDict[speech.text].Invoke();
  }

  private void greet()
  {
    print("hello there");
  }
}
