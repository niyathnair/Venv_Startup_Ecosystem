from agents.rag_agents.strategy_leadership.data_processing.performance_analyzer import PerformanceAnalyzer
from agents.rag_agents.strategy_leadership.models.strategy_model import StrategyModel
from agents.rag_agents.strategy_leadership.retrieval.strategy_retriever import StrategyRetriever
from shared_components.communication_hub import CommunicationHub
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StrategyLeadershipAgent:
    def __init__(self, knowledge_base_path, communication_hub):
        """
        Initialize the StrategyLeadershipAgent with components and communication hub.
        """
        self.retriever = StrategyRetriever(knowledge_base_path)
        self.analyzer = PerformanceAnalyzer()
        self.strategy_model = StrategyModel()
        self.communication_hub = communication_hub
        self.performance_records = {}
        self.improvement_history = {}
        self.performance_threshold = 75.0

    def evaluate_organization_performance(self, performance_data):
        """
        Evaluate the performance of all departments and take necessary actions.
        """
        logger.info("Evaluating organization performance...")
        for record in performance_data:
            department = record['department']
            score = record['performance_score']
            weak_areas = record.get('weak_areas', [])
            self.performance_records[department] = score

            if score < self.performance_threshold:
                self.send_improvement_plan(department, weak_areas)
                self.send_penalty(department, "Underperformance")
            else:
                self.send_reward(department, "Excellent performance")

        return self.performance_records

    def generate_summary(self, performance_data):
        """
        Generates a performance summary.
        """
        return self.analyzer.generate_performance_summary(performance_data)

    def formulate_strategic_plans(self, performance_data):
        """
        Formulates strategic plans based on performance data.
        """
        return self.strategy_model.develop_strategies(performance_data)

    def create_executive_report(self, summary):
        """
        Creates executive reports from the performance summary.
        """
        return self.strategy_model.create_reports(summary)

    def search_performance_records(self, query):
        """
        Searches for performance records using the retriever.
        """
        return self.retriever.retrieve_performance_data(query)

    def send_penalty(self, department, reason):
        """
        Sends a penalty message to a department.
        """
        message = {
            "action": "penalty",
            "reason": reason
        }
        self.communication_hub.send_message("StrategyLeadershipAgent", department, message)
        logger.info(f"Penalty sent to {department} for {reason}.")

    def send_reward(self, department, reason):
        """
        Sends a reward message to a department.
        """
        message = {
            "action": "reward",
            "reason": reason
        }
        self.communication_hub.send_message("StrategyLeadershipAgent", department, message)
        logger.info(f"Reward sent to {department} for {reason}.")

    def send_improvement_plan(self, department, weak_areas):
        """
        Sends an improvement plan to a department.
        """
        plan = {
            "action": "improve",
            "weak_areas": weak_areas,
            "guidance": "Develop specific plans to address these areas."
        }
        self.communication_hub.send_message("StrategyLeadershipAgent", department, plan)
        self.improvement_history.setdefault(department, []).append(plan)
        logger.info(f"Improvement plan sent to {department} for weak areas: {weak_areas}.")

    def receive_message(self, sender, message):
        """
        Handles incoming messages from agents.
        """
        logger.info(f"[StrategyLeadershipAgent] Received message from {sender}: {message}")

        # Check if the message contains a performance update request
        if message.get("request") == "performance_update":
            department = message.get("department", sender)
            score = message.get("performance_score", -1)

            # Ensure performance score is valid
            if score == -1:
                logger.error(f"Invalid performance score from {sender}: {message}")
                return

            # Record performance
            self.performance_records[department] = score
            logger.info(f"Recorded performance for {department}: {score}")

            # Handle performance evaluation
            kpis = message.get("kpis", {})
            weak_areas = kpis.get("weak_areas", [])

            if kpis.get("status") == "Below Threshold":
                self.send_improvement_plan(department, weak_areas)
                self.send_penalty(department, "Underperformance")
            else:
                self.send_reward(department, "Excellent performance")
        else:
            logger.warning(f"Unsupported message format received from {sender}.")
