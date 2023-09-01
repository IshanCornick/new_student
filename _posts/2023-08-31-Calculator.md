---
toc: true
comments: false
layout: post
title: Calculator
description: Example Blog!!!  This shows planning and notes from hacks.
type: hacks
courses: { compsci: {week: 0} }
---
<style>
  button {
    width: 100px;
    height: 100px;
    color: blue;
    background-color: grey;
    font-size: 35px;
  }
</style>
<html>
<body>
  <input type="text" id="display" readonly>
  <br>
  <button onclick="appendToDisplay('1')">1</button>
  <button onclick="appendToDisplay('2')">2</button>
  <button onclick="appendToDisplay('3')">3</button>
  <button onclick="appendToDisplay('+')">+</button>
  <br>
  <button onclick="appendToDisplay('4')">4</button>
  <button onclick="appendToDisplay('5')">5</button>
  <button onclick="appendToDisplay('6')">6</button>
  <button onclick="appendToDisplay('-')">-</button>
  <br>
  <button onclick="appendToDisplay('7')">7</button>
  <button onclick="appendToDisplay('8')">8</button>
  <button onclick="appendToDisplay('9')">9</button>
  <button onclick="appendToDisplay('*')">*</button>
  <br>
  <button onclick="appendToDisplay('0')">0</button>
  <button onclick="clearDisplay()">C</button>
  <button onclick="calculate()">=</button>
  <button onclick="appendToDisplay('/')">/</button>
  
  <script>
    let displayValue = '';
    function appendToDisplay(value) {
      displayValue += value;
      document.getElementById('display').value = displayValue;
    }
    function clearDisplay() {
      displayValue = '';
      document.getElementById('display').value = displayValue;
    }
    
    function calculate() {
      try {
        displayValue = eval(displayValue);
        document.getElementById('display').value = displayValue;
      } catch (error) {
        document.getElementById('display').value = 'Error';
      }
    }
  </script>
</body>
</html>
