from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import EXASearchTool

@CrewBase
class InsightsCrewCrew():
	"""InsightsCrew crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def business_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['business_researcher'],
			tools=[EXASearchTool()],
			verbose=True
		)

	@agent
	def tech_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['tech_researcher'],
   			tools=[EXASearchTool()],
			verbose=True
		)

	@agent
	def management_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['management_researcher'],
			tools=[EXASearchTool()],
			verbose=True
		)

	@agent
	def knowledge_graph_engineer(self) -> Agent:
		return Agent(
			config=self.agents_config['knowledge_graph_engineer'],
			verbose=True
		)

	@agent
	def research_insights(self) -> Agent:
		return Agent(
			config=self.agents_config['research_insights'],
			verbose=True
		)

	@task
	def business_task(self) -> Task:
		return Task(
			config=self.tasks_config['business_task'],
			agent=self.business_researcher()
		)

	@task
	def tech_task(self) -> Task:
		return Task(
			config=self.tasks_config['tech_task'],
			agent=self.tech_researcher(),
		)

	@task
	def management_task(self) -> Task:
		return Task(
			config=self.tasks_config['management_task'],
			agent=self.management_researcher()
		)

	@task
	def kg_task(self) -> Task:
		return Task(
			config=self.tasks_config['kg_task'],
			agent=self.knowledge_graph_engineer(),
			output_file='graph.md'
		)

	@task
	def report_task(self) -> Task:
		return Task(
			config=self.tasks_config['report_task'],
			agent=self.research_insights(),
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the InsightsCrew crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=2,
		)