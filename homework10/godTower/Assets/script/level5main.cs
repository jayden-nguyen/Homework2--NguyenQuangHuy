using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
public class level5main : MonoBehaviour
{
    public Text levelText;
    public Text hinText;
    public string levelContent = "LEVELS";
    public string levelNumber;
    public InputField inputField;
    public Button submitButton;
    public string levelAnswer;
    string answer;
    // Use this for initialization
    void Start()
    {
        levelText.text = levelContent;
        StartCoroutine(ChangeLevelTextRoutine());
    }
    public void GetInput()
    {
        answer = inputField.text;
        CheckAnswer(answer.ToLower());
    }
    public void CheckAnswer(string answer)
    {
        if (answer == levelAnswer)
        {
            hinText.text = "Yayyyy";
            //TODO: Change scene
            //SceneManager.LoadScene(3);
        }
        else
        {
            hinText.text = "WRONGGGG!!!!!";
            hinText.color = Color.red;
            inputField.text = "";
            inputField.ActivateInputField();
        }
    }
    IEnumerator ChangeLevelTextRoutine()
    {
        while (true)
        {
            levelText.text = levelContent;
            //Wait for 2 seconds
            yield return new WaitForSeconds(2f);
            levelText.text = levelNumber;
            yield return new WaitForSeconds(2f);
        }

    }
    // Update is called once per frame
    void Update()
    {

    }
}
