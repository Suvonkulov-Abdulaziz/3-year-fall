package com.example.financetracker.ui.screens

import androidx.compose.foundation.layout.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import com.example.financetracker.ui.theme.*

@Composable
fun HomeScreen(navController: NavController) {
    var balance by remember { mutableStateOf(0.0) }
    var income by remember { mutableStateOf(0.0) }
    var expenses by remember { mutableStateOf(0.0) }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Finance Tracker") },
                actions = {
                    IconButton(onClick = { navController.navigate("settings") }) {
                        Icon(Icons.Default.Settings, contentDescription = "Settings")
                    }
                }
            )
        },
        bottomBar = {
            NavigationBar {
                NavigationBarItem(
                    icon = { Icon(Icons.Default.Home, contentDescription = "Home") },
                    label = { Text("Home") },
                    selected = true,
                    onClick = { navController.navigate("home") }
                )
                NavigationBarItem(
                    icon = { Icon(Icons.Default.List, contentDescription = "Transactions") },
                    label = { Text("Transactions") },
                    selected = false,
                    onClick = { navController.navigate("transactions") }
                )
                NavigationBarItem(
                    icon = { Icon(Icons.Default.CreditCard, contentDescription = "Cards") },
                    label = { Text("Cards") },
                    selected = false,
                    onClick = { navController.navigate("cards") }
                )
                NavigationBarItem(
                    icon = { Icon(Icons.Default.PieChart, contentDescription = "Statistics") },
                    label = { Text("Statistics") },
                    selected = false,
                    onClick = { navController.navigate("statistics") }
                )
            }
        }
    ) { paddingValues ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues)
                .padding(16.dp),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            // Balance Card
            Card(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(vertical = 8.dp),
                colors = CardDefaults.cardColors(containerColor = CardBackground)
            ) {
                Column(
                    modifier = Modifier.padding(16.dp),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Text(
                        text = "Total Balance",
                        style = MaterialTheme.typography.titleLarge,
                        color = TextSecondary
                    )
                    Text(
                        text = "$${balance.format(2)}",
                        style = MaterialTheme.typography.displayLarge,
                        color = TextPrimary
                    )
                }
            }

            // Income/Expense Cards
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(vertical = 8.dp),
                horizontalArrangement = Arrangement.SpaceEvenly
            ) {
                // Income Card
                Card(
                    modifier = Modifier
                        .weight(1f)
                        .padding(end = 4.dp),
                    colors = CardDefaults.cardColors(containerColor = IncomeGreen)
                ) {
                    Column(
                        modifier = Modifier.padding(16.dp),
                        horizontalAlignment = Alignment.CenterHorizontally
                    ) {
                        Text(
                            text = "Income",
                            style = MaterialTheme.typography.titleLarge,
                            color = Color.White
                        )
                        Text(
                            text = "$${income.format(2)}",
                            style = MaterialTheme.typography.displayMedium,
                            color = Color.White
                        )
                    }
                }

                // Expense Card
                Card(
                    modifier = Modifier
                        .weight(1f)
                        .padding(start = 4.dp),
                    colors = CardDefaults.cardColors(containerColor = ExpenseRed)
                ) {
                    Column(
                        modifier = Modifier.padding(16.dp),
                        horizontalAlignment = Alignment.CenterHorizontally
                    ) {
                        Text(
                            text = "Expenses",
                            style = MaterialTheme.typography.titleLarge,
                            color = Color.White
                        )
                        Text(
                            text = "$${expenses.format(2)}",
                            style = MaterialTheme.typography.displayMedium,
                            color = Color.White
                        )
                    }
                }
            }

            // Quick Actions
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(vertical = 16.dp),
                horizontalArrangement = Arrangement.SpaceEvenly
            ) {
                QuickActionButton(
                    icon = Icons.Default.Add,
                    text = "Add Income",
                    onClick = { /* TODO: Implement add income */ }
                )
                QuickActionButton(
                    icon = Icons.Default.Remove,
                    text = "Add Expense",
                    onClick = { /* TODO: Implement add expense */ }
                )
                QuickActionButton(
                    icon = Icons.Default.CreditCard,
                    text = "Add Card",
                    onClick = { navController.navigate("cards") }
                )
            }
        }
    }
}

@Composable
fun QuickActionButton(
    icon: androidx.compose.ui.graphics.vector.ImageVector,
    text: String,
    onClick: () -> Unit
) {
    Column(
        horizontalAlignment = Alignment.CenterHorizontally,
        modifier = Modifier.padding(8.dp)
    ) {
        IconButton(onClick = onClick) {
            Icon(icon, contentDescription = text)
        }
        Text(
            text = text,
            style = MaterialTheme.typography.labelSmall,
            textAlign = TextAlign.Center
        )
    }
}

fun Double.format(digits: Int) = "%.${digits}f".format(this) 