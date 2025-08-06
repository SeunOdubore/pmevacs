import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

void main() => runApp(VoteBoostApp());

class VoteBoostApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'VoteBoost NG',
      theme: ThemeData(primarySwatch: Colors.green),
      home: HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  var result;

  Future<void> predict() async {
    final body = {
      "age": 22,
      "gender": "M",
      "location": "Lagos",
      "education": "University",
      "employment": "Yes",
      "voter_registered": 1,
      "social_media_use": "High",
      "political_interest": "Medium"
    };

    final response = await http.post(
      Uri.parse('http://your-server.com/predict'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode(body),
    );

    if (response.statusCode == 200) {
      setState(() {
        result = jsonDecode(response.body);
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("VoteBoost NG 🇳🇬")),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          children: [
            ElevatedButton(
              onPressed: predict,
              child: Text("Check My Voting Score"),
            ),
            if (result != null) ...[
              Text("Likelihood: ${(result['voting_likelihood'] * 100).toStringAsFixed(1)}%"),
              Text("Risk: ${result['apathy_risk']}"),
              Text("Tip: ${result['recommendation']}"),
            ]
          ],
        ),
      ),
      bottomNavigationBar: BottomNavBar(),
    );
  }
}

class BottomNavBar extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return BottomNavigationBar(
      items: [
        BottomNavigationBarItem(icon: Icon(Icons.home), label: "Home"),
        BottomNavigationBarItem(icon: Icon(Icons.quiz), label: "Quiz"),
        BottomNavigationBarItem(icon: Icon(Icons.leaderboard), label: "Rank"),
      ],
    );
  }
}