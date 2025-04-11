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
import com.example.financetracker.data.Transaction
import com.example.financetracker.data.TransactionType
import com.example.financetracker.ui.theme.*
import com.github.mikephil.charting.charts.PieChart
import com.github.mikephil.charting.data.PieData
import com.github.mikephil.charting.data.PieDataSet
import com.github.mikephil.charting.data.PieEntry
import java.util.*

@Composable
fun StatisticsScreen(navController: NavController) {
    var transactions by remember { mutableStateOf(listOf<Transaction>()) }
    var selectedPeriod by remember { mutableStateOf("Month") }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Statistics") },
                navigationIcon = {
                    IconButton(onClick = { navController.navigateUp() }) {
                        Icon(Icons.Default.ArrowBack, contentDescription = "Back")
                    }
                }
            )
        }
    ) { paddingValues ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues)
        ) {
            // Period Selection
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(16.dp),
                horizontalArrangement = Arrangement.SpaceEvenly
            ) {
                FilterChip(
                    selected = selectedPeriod == "Week",
                    onClick = { selectedPeriod = "Week" },
                    label = { Text("Week") }
                )
                FilterChip(
                    selected = selectedPeriod == "Month",
                    onClick = { selectedPeriod = "Month" },
                    label = { Text("Month") }
                )
                FilterChip(
                    selected = selectedPeriod == "Year",
                    onClick = { selectedPeriod = "Year" },
                    label = { Text("Year") }
                )
            }

            // Pie Chart
            Card(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(16.dp)
                    .height(300.dp),
                colors = CardDefaults.cardColors(containerColor = CardBackground)
            ) {
                Box(
                    modifier = Modifier.fillMaxSize(),
                    contentAlignment = Alignment.Center
                ) {
                    PieChartView(transactions = transactions)
                }
            }

            // Category Breakdown
            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(16.dp)
            ) {
                Text(
                    text = "Category Breakdown",
                    style = MaterialTheme.typography.titleLarge,
                    modifier = Modifier.padding(bottom = 16.dp)
                )

                // Calculate category totals
                val categoryTotals = transactions
                    .filter { it.type == TransactionType.EXPENSE }
                    .groupBy { it.category }
                    .mapValues { (_, transactions) -> transactions.sumOf { it.amount } }
                    .toList()
                    .sortedByDescending { it.second }

                categoryTotals.forEach { (category, amount) ->
                    CategoryItem(
                        category = category,
                        amount = amount,
                        percentage = (amount / categoryTotals.sumOf { it.second } * 100).toInt()
                    )
                }
            }
        }
    }
}

@Composable
fun PieChartView(transactions: List<Transaction>) {
    // Calculate category totals for expenses
    val categoryTotals = transactions
        .filter { it.type == TransactionType.EXPENSE }
        .groupBy { it.category }
        .mapValues { (_, transactions) -> transactions.sumOf { it.amount } }

    // Create pie chart entries
    val entries = categoryTotals.map { (category, amount) ->
        PieEntry(amount.toFloat(), category)
    }

    // Create pie chart dataset
    val dataSet = PieDataSet(entries, "Expenses by Category").apply {
        colors = listOf(
            Color(0xFF4CAF50).hashCode(),
            Color(0xFF2196F3).hashCode(),
            Color(0xFFFFC107).hashCode(),
            Color(0xFFF44336).hashCode(),
            Color(0xFF9C27B0).hashCode()
        )
        valueTextSize = 12f
    }

    // Create pie chart data
    val data = PieData(dataSet)

    // Create and configure pie chart
    AndroidView(
        factory = { context ->
            PieChart(context).apply {
                data = data
                description.isEnabled = false
                legend.isEnabled = true
                setDrawEntryLabels(false)
                setHoleColor(android.graphics.Color.TRANSPARENT)
                setTransparentCircleAlpha(0)
                animateY(1000)
            }
        },
        modifier = Modifier.fillMaxSize()
    )
}

@Composable
fun CategoryItem(category: String, amount: Double, percentage: Int) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .padding(vertical = 8.dp),
        horizontalArrangement = Arrangement.SpaceBetween,
        verticalAlignment = Alignment.CenterVertically
    ) {
        Text(
            text = category,
            style = MaterialTheme.typography.bodyLarge
        )
        Row(
            horizontalArrangement = Arrangement.spacedBy(16.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            Text(
                text = "$percentage%",
                style = MaterialTheme.typography.bodyLarge,
                color = TextSecondary
            )
            Text(
                text = "$${amount.format(2)}",
                style = MaterialTheme.typography.bodyLarge,
                color = TextPrimary
            )
        }
    }
} 