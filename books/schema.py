import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Quizzes, Category, Question, Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name')

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ('id', 'title', 'category', 'quiz')

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ('title', 'quiz')

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ('answer_text', 'question', 'id')

class Query(graphene.ObjectType):
    all_quizzes = DjangoListField(QuizzesType)
    question = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())

    def resolve_all_quizzes(root, info):
        return Quizzes.objects.filter(id=1)

    def resolve_question(root, info, id):
        return Question.objects.get(pk=id)

    def resolve_all_answers(root, info, id):
            return Answer.objects.filter(id = id)

# class CategoryMutation(graphene.Mutation):
#     class Arguments:
#         name = graphene.String(required=True)
#
#     category = graphene.Field(CategoryType)
#
#     @classmethod
#     def mutate(cls, root, info, name):
#         category=Category(name=name)
#         category.save()
#         return CategoryMutation(category=category)

class CategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()


    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
            category = Category.objects.get(id=id)
            category.delete()
            return CategoryMutation(category=category)

class Mutation(graphene.ObjectType):
    update_category = CategoryMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
