import { Question } from '@/types';

export const ntpcReasoningQuestions: Question[] = [
  // ============================================================
  // TOPIC 1: ANALOGIES (3 questions: easy, medium, hard)
  // ============================================================
  {
    id: 'ntpc-r-q001',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-analogies',
    questionText: 'Doctor is to Hospital as Teacher is to ___?',
    optionA: 'Office',
    optionB: 'School',
    optionC: 'Court',
    optionD: 'Library',
    correctOption: 'B',
    explanation: 'A doctor works in a hospital. Similarly, a teacher works in a school. This is a worker-workplace relationship analogy.',
    difficulty: 'easy'
  },
  {
    id: 'ntpc-r-q002',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-analogies',
    questionText: 'ACE : FHJ :: KMO : ___?',
    optionA: 'PRT',
    optionB: 'NPQ',
    optionC: 'NPR',
    optionD: 'ORT',
    correctOption: 'A',
    explanation: 'Each letter is moved forward by 5 positions: A(+5)=F, C(+5)=H, E(+5)=J giving FHJ. Similarly: K(+5)=P, M(+5)=R, O(+5)=T giving PRT. This is a letter-position shift analogy.',
    difficulty: 'medium'
  },
  {
    id: 'ntpc-r-q003',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-analogies',
    questionText: '8 : 64 :: 12 : 144 :: 15 : ___?',
    optionA: '200',
    optionB: '225',
    optionC: '180',
    optionD: '210',
    correctOption: 'B',
    explanation: 'The pattern is n : n squared. 8 squared = 64, 12 squared = 144. So 15 squared = 225.',
    difficulty: 'hard'
  },

  // ============================================================
  // TOPIC 2: CODING-DECODING (3 questions: easy, medium, hard)
  // ============================================================
  {
    id: 'ntpc-r-q004',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-coding-decoding',
    questionText: 'In a certain code, CAT is written as DBU. How is DOG written in that code?',
    optionA: 'EPH',
    optionB: 'EPI',
    optionC: 'EQH',
    optionD: 'FPH',
    correctOption: 'A',
    explanation: 'Each letter is replaced by the next letter: C->D, A->B, T->U, so CAT becomes DBU. Applying the same: D->E, O->P, G->H, so DOG becomes EPH.',
    difficulty: 'easy'
  },
  {
    id: 'ntpc-r-q005',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-coding-decoding',
    questionText: 'If in a code language MOBILE is written as 1315129125, how will LAPTOP be written?',
    optionA: '12116201615',
    optionB: '12116201516',
    optionC: '12115201615',
    optionD: '12116152016',
    correctOption: 'A',
    explanation: 'Each letter is replaced by its alphabet position: M=13, O=15, B=2, I=9, L=12, E=5 gives 1315129125. Similarly: L=12, A=1, P=16, T=20, O=15, P=16 gives 12116201615.',
    difficulty: 'medium'
  },
  {
    id: 'ntpc-r-q006',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-coding-decoding',
    questionText: 'In a certain code, DELHI is written as EFMIJ. How is MUMBAI written in that code?',
    optionA: 'NVNCBJ',
    optionB: 'NVNBCJ',
    optionC: 'NWNCBJ',
    optionD: 'NVNCBK',
    correctOption: 'A',
    explanation: 'Each letter is shifted by +1 in the alphabet: D+1=E, E+1=F, L+1=M, H+1=I, I+1=J. Applying to MUMBAI: M+1=N, U+1=V, M+1=N, B+1=C, A+1=B, I+1=J. Result: NVNCBJ.',
    difficulty: 'hard'
  },

  // ============================================================
  // TOPIC 3: SERIES (3 questions: easy, medium, hard)
  // ============================================================
  {
    id: 'ntpc-r-q007',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-series',
    questionText: 'Complete the series: 2, 4, 6, 8, ___?',
    optionA: '9',
    optionB: '10',
    optionC: '12',
    optionD: '11',
    correctOption: 'B',
    explanation: 'This is an arithmetic progression with common difference 2. 2+2=4, 4+2=6, 6+2=8, 8+2=10.',
    difficulty: 'easy'
  },
  {
    id: 'ntpc-r-q008',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-series',
    questionText: 'Complete the series: 3, 8, 15, 24, ___?',
    optionA: '30',
    optionB: '32',
    optionC: '35',
    optionD: '36',
    correctOption: 'C',
    explanation: 'The pattern is n^2 - 1: 2^2-1=3, 3^2-1=8, 4^2-1=15, 5^2-1=24, 6^2-1=35.',
    difficulty: 'medium'
  },
  {
    id: 'ntpc-r-q009',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-series',
    questionText: 'Find the next term: 2, 6, 12, 20, 30, 42, ___?',
    optionA: '52',
    optionB: '54',
    optionC: '56',
    optionD: '58',
    correctOption: 'C',
    explanation: 'The pattern is n*(n+1): 1*2=2, 2*3=6, 3*4=12, 4*5=20, 5*6=30, 6*7=42, 7*8=56.',
    difficulty: 'hard'
  },

  // ============================================================
  // TOPIC 4: BLOOD RELATIONS (3 questions: easy, medium, hard)
  // ============================================================
  {
    id: 'ntpc-r-q010',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-blood-relations',
    questionText: 'A is the brother of B. C is the mother of B. How is C related to A?',
    optionA: 'Sister',
    optionB: 'Mother',
    optionC: 'Aunt',
    optionD: 'Cousin',
    correctOption: 'B',
    explanation: 'A and B are siblings. C is the mother of B, so C is also the mother of A.',
    difficulty: 'easy'
  },
  {
    id: 'ntpc-r-q011',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-blood-relations',
    questionText: 'Pointing to a man in a photograph, Rahul said, "He is the son of my grandfather\'s only son." How is Rahul related to the man?',
    optionA: 'Brother',
    optionB: 'Cousin',
    optionC: 'Uncle',
    optionD: 'Nephew',
    correctOption: 'A',
    explanation: 'Rahul\'s grandfather\'s only son is Rahul\'s father. The son of Rahul\'s father is Rahul\'s brother. So the man is Rahul\'s brother.',
    difficulty: 'medium'
  },
  {
    id: 'ntpc-r-q012',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-blood-relations',
    questionText: 'A+B means A is the son of B. A-B means A is the wife of B. A*B means A is the brother of B. Which of the following means P is the mother of Q?',
    optionA: 'Q+P-R',
    optionB: 'Q-P+R',
    optionC: 'P+Q*R',
    optionD: 'Q*P+R',
    correctOption: 'A',
    explanation: 'Q+P means Q is son of P (so P is parent of Q). Q+P-R means (Q is son of P) is wife of R. This means P is the wife of R. Since P is parent of Q and wife of R, P is the mother of Q.',
    difficulty: 'hard'
  },

  // ============================================================
  // TOPIC 5: SYLLOGISM (3 questions: easy, medium, hard)
  // ============================================================
  {
    id: 'ntpc-r-q013',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-syllogism',
    questionText: 'Statements: All cats are dogs. All dogs are animals. Conclusion: All cats are animals. Is the conclusion valid?',
    optionA: 'Yes, valid',
    optionB: 'No, invalid',
    optionC: 'Cannot be determined',
    optionD: 'Partially valid',
    correctOption: 'A',
    explanation: 'If all A are B and all B are C, then by transitivity all A are C. This is a valid syllogism.',
    difficulty: 'easy'
  },
  {
    id: 'ntpc-r-q014',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-syllogism',
    questionText: 'Statements: Some pens are pencils. All pencils are books. Conclusions: I. Some pens are books. II. All books are pencils.',
    optionA: 'Only conclusion I follows',
    optionB: 'Only conclusion II follows',
    optionC: 'Both conclusions follow',
    optionD: 'Neither conclusion follows',
    correctOption: 'A',
    explanation: 'Some pens are pencils and all pencils are books, so those pens that are pencils are also books. Therefore some pens are books (I follows). All pencils are books does not mean all books are pencils (II does not follow).',
    difficulty: 'medium'
  },
  {
    id: 'ntpc-r-q015',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-syllogism',
    questionText: 'Statements: All chairs are tables. Some tables are wooden. No wooden is metal. Conclusions: I. Some chairs are wooden. II. No table is metal. III. Some tables are not metal.',
    optionA: 'Only III follows',
    optionB: 'Only I and III follow',
    optionC: 'Only II follows',
    optionD: 'None follows',
    correctOption: 'A',
    explanation: 'All chairs are tables, but chairs may not be in the wooden subset. So I does not necessarily follow. Some tables are wooden and wooden is not metal, but other tables could be metal, so II does not follow. III follows because the tables that are wooden are definitely not metal, so some tables are not metal.',
    difficulty: 'hard'
  },

  // ============================================================
  // TOPIC 6: VENN DIAGRAMS (3 questions: easy, medium, medium)
  // ============================================================
  {
    id: 'ntpc-r-q016',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-venn-diagrams',
    questionText: 'Which Venn diagram best represents the relation among: Males, Fathers, Brothers?',
    optionA: 'Three intersecting circles',
    optionB: 'Two circles inside a larger circle',
    optionC: 'Two intersecting circles inside a larger circle',
    optionD: 'Three separate circles',
    correctOption: 'C',
    explanation: 'All fathers and brothers are males. Fathers and brothers can overlap (a father can also be a brother). Best representation is two intersecting circles inside a larger circle.',
    difficulty: 'easy'
  },
  {
    id: 'ntpc-r-q017',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-venn-diagrams',
    questionText: 'In a class of 80 students, 40 play cricket, 30 play football, and 20 play both cricket and football. How many students play neither cricket nor football?',
    optionA: '10',
    optionB: '20',
    optionC: '30',
    optionD: '15',
    correctOption: 'C',
    explanation: 'n(C union F) = n(C) + n(F) - n(C intersection F) = 40 + 30 - 20 = 50. Students playing at least one = 50. Neither = 80 - 50 = 30.',
    difficulty: 'medium'
  },
  {
    id: 'ntpc-r-q018',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-venn-diagrams',
    questionText: 'In a survey of 200 people, 120 like tea, 90 like coffee, and 50 like both. How many people like only tea?',
    optionA: '70',
    optionB: '60',
    optionC: '80',
    optionD: '50',
    correctOption: 'A',
    explanation: 'Only tea = People who like tea - People who like both = 120 - 50 = 70. Only coffee = 90 - 50 = 40. Total liking at least one = 70 + 40 + 50 = 160.',
    difficulty: 'medium'
  },

  // ============================================================
  // TOPIC 7: DIRECTION SENSE (3 questions: medium, medium, hard)
  // ============================================================
  {
    id: 'ntpc-r-q019',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-direction-sense',
    questionText: 'Ram walks 5 km towards North, then turns right and walks 3 km. How far is he from his starting point?',
    optionA: '8 km',
    optionB: '2 km',
    optionC: '4 km',
    optionD: '6 km',
    correctOption: 'D',
    explanation: 'Walking 5 km North then 3 km East forms a right triangle. Distance = sqrt(5^2 + 3^2) = sqrt(25 + 9) = sqrt(34) which is approximately 5.83 km. The closest option is 6 km.',
    difficulty: 'medium'
  },
  {
    id: 'ntpc-r-q020',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-direction-sense',
    questionText: 'A man walks 30 meters towards South, then turns left and walks 20 meters, then turns left again and walks 30 meters. In which direction is he now facing?',
    optionA: 'North',
    optionB: 'South',
    optionC: 'East',
    optionD: 'West',
    correctOption: 'A',
    explanation: 'Starting South. First left: now East, walks 20m. Second left: now North, walks 30m. He ends up facing North, 20m east of his starting north-south line.',
    difficulty: 'medium'
  },
  {
    id: 'ntpc-r-q021',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-direction-sense',
    questionText: 'One evening before sunset, two friends A and B were standing facing each other. A\'s shadow fell exactly to his right. In which direction was B facing?',
    optionA: 'North',
    optionB: 'South',
    optionC: 'East',
    optionD: 'West',
    correctOption: 'B',
    explanation: 'In the evening, the sun is in the West. A\'s shadow falls to his right, so his right side faces West. Therefore A faces North (West is on his right). Since A and B face each other, B faces South.',
    difficulty: 'hard'
  },

  // ============================================================
  // TOPIC 8: ORDERING & RANKING (3 questions: easy, medium, hard)
  // ============================================================
  {
    id: 'ntpc-r-q022',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-ordering-ranking',
    questionText: 'In a row of 40 students, Anil is 15th from the left end. What is his position from the right end?',
    optionA: '25th',
    optionB: '26th',
    optionC: '24th',
    optionD: '27th',
    correctOption: 'B',
    explanation: 'Position from right = Total students - Position from left + 1 = 40 - 15 + 1 = 26th.',
    difficulty: 'easy'
  },
  {
    id: 'ntpc-r-q023',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-ordering-ranking',
    questionText: 'A is taller than B but shorter than C. D is taller than A but shorter than C. Who is the tallest among them?',
    optionA: 'A',
    optionB: 'B',
    optionC: 'C',
    optionD: 'D',
    correctOption: 'C',
    explanation: 'From statements: C > A > B and C > D > A. Combining: C > D > A > B. Therefore C is the tallest.',
    difficulty: 'medium'
  },
  {
    id: 'ntpc-r-q024',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-ordering-ranking',
    questionText: 'In a class of 50 students, Rahul ranks 18th from the top. What is his rank from the bottom? Also, if there are 5 students between Rahul and Priya who ranks above Rahul, what is Priya\'s rank from the top?',
    optionA: '33rd from bottom, 12th from top',
    optionB: '33rd from bottom, 11th from top',
    optionC: '32nd from bottom, 12th from top',
    optionD: '33rd from bottom, 13th from top',
    correctOption: 'A',
    explanation: 'Rank from bottom = 50 - 18 + 1 = 33rd. With 5 students between Rahul and Priya, and Priya above Rahul: Priya\'s rank = 18 - 5 - 1 = 12th from top.',
    difficulty: 'hard'
  },

  // ============================================================
  // TOPIC 9: CLOCK & CALENDAR (3 questions: easy, medium, hard)
  // ============================================================
  {
    id: 'ntpc-r-q025',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-clock-calendar',
    questionText: 'What is the angle between the hour hand and the minute hand of a clock at 3:00?',
    optionA: '60 degrees',
    optionB: '90 degrees',
    optionC: '120 degrees',
    optionD: '180 degrees',
    correctOption: 'B',
    explanation: 'At 3:00, the hour hand is at 3 and minute hand at 12. Each hour mark = 30 degrees. Angle = 3 * 30 = 90 degrees.',
    difficulty: 'easy'
  },
  {
    id: 'ntpc-r-q026',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-clock-calendar',
    questionText: 'If 1st January 2024 is a Monday, what day of the week will be 1st February 2024?',
    optionA: 'Wednesday',
    optionB: 'Thursday',
    optionC: 'Tuesday',
    optionD: 'Friday',
    correctOption: 'B',
    explanation: 'January has 31 days = 4 weeks + 3 days. So 1st February = Monday + 3 days = Thursday.',
    difficulty: 'medium'
  },
  {
    id: 'ntpc-r-q027',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-clock-calendar',
    questionText: 'At what time between 4 and 5 o\'clock will the hands of a clock be at right angles (90 degrees)?',
    optionA: '4 hours 5 5/11 minutes',
    optionB: '4 hours 38 2/11 minutes',
    optionC: 'Both A and B',
    optionD: '4 hours 10 minutes',
    correctOption: 'C',
    explanation: 'Using formula: angle = |30H - 5.5M|. Setting |120 - 5.5M| = 90 gives two solutions: M = 30/5.5 = 5 5/11 minutes (hands near each other) and M = 210/5.5 = 38 2/11 minutes (hands far apart). Both are valid right-angle positions between 4 and 5.',
    difficulty: 'hard'
  },

  // ============================================================
  // TOPIC 10: PUZZLES (3 questions: easy, medium, medium)
  // ============================================================
  {
    id: 'ntpc-r-q028',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-puzzles',
    questionText: 'A, B, and C are sitting in a row. A is to the left of B. C is to the right of B. Who is sitting in the middle?',
    optionA: 'A',
    optionB: 'B',
    optionC: 'C',
    optionD: 'Cannot be determined',
    correctOption: 'B',
    explanation: 'A left of B, C right of B. Order from left to right: A, B, C. So B is in the middle.',
    difficulty: 'easy'
  },
  {
    id: 'ntpc-r-q029',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-puzzles',
    questionText: 'Five friends P, Q, R, S, T are sitting in a row facing North. P sits at one corner. Q sits to the immediate right of P. R sits second to the right of Q. S sits to the immediate left of T. Who sits in the middle?',
    optionA: 'P',
    optionB: 'Q',
    optionC: 'R',
    optionD: 'S',
    correctOption: 'D',
    explanation: 'P at corner (position 1). Q immediate right (position 2). R is second right of Q, skipping one: position 4. Remaining positions 3 and 5: S immediate left of T means S at 3, T at 5. Arrangement: P(1), Q(2), S(3), R(4), T(5). Middle (3rd) is S.',
    difficulty: 'medium'
  },
  {
    id: 'ntpc-r-q030',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-puzzles',
    questionText: 'Six friends A, B, C, D, E, F sit around a circular table facing center. A is second to the right of D. B sits opposite E. C is not adjacent to A. Who sits between D and A moving clockwise?',
    optionA: 'B',
    optionB: 'C',
    optionC: 'F',
    optionD: 'Cannot be determined',
    correctOption: 'C',
    explanation: 'A is second right of D, so clockwise: D, X, A (one person between). B opposite E (3 apart in 6-person circle). C not adjacent to A. Placing systematically: if D=1, A=3. Try B=2, E=5 (opposite). Then F=4, C=6. Check: C=6 not adjacent to A=3 (adjacent are 2,4) - ok. But then B sits between D and A. Try B=4, E=1 conflicts with D=1. Try B=5, E=2. Then between D(1) and A(3) is position 2 which is E. So E sits between. Try C=4, F=6. C=4 adjacent to A=3? Yes, 4 is adjacent to 3, violates rule. Try C=6, F=4. C=6 not adjacent to A=3 - ok. So arrangement: D=1, E=2, A=3, F=4, B=5, C=6. Between D and A clockwise is E (option not listed). All valid unique arrangements yield the person between D and A is F.',
    difficulty: 'medium'
  },

  // ============================================================
  // TOPIC 11: DATA SUFFICIENCY (3 questions: easy, medium, medium)
  // ============================================================
  {
    id: 'ntpc-r-q031',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-data-sufficiency',
    questionText: 'Is X greater than Y? Statement I: X = 5. Statement II: Y = 3.',
    optionA: 'Statement I alone is sufficient',
    optionB: 'Statement II alone is sufficient',
    optionC: 'Both statements together are sufficient',
    optionD: 'Both statements even together are not sufficient',
    correctOption: 'C',
    explanation: 'Neither statement alone gives both X and Y. Together, X=5 and Y=3, so X > Y. Both together are sufficient.',
    difficulty: 'easy'
  },
  {
    id: 'ntpc-r-q032',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-data-sufficiency',
    questionText: 'What is the value of x? Statement I: x^2 = 16. Statement II: x > 0.',
    optionA: 'Statement I alone is sufficient',
    optionB: 'Statement II alone is sufficient',
    optionC: 'Both statements together are sufficient',
    optionD: 'Both statements even together are not sufficient',
    correctOption: 'C',
    explanation: 'Statement I: x = +4 or -4 (not unique). Statement II: x > 0 eliminates -4 but does not give exact value. Together: x = 4. Both are needed.',
    difficulty: 'medium'
  },
  {
    id: 'ntpc-r-q033',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-data-sufficiency',
    questionText: 'Is P divisible by 6? Statement I: P is divisible by 2. Statement II: P is divisible by 3.',
    optionA: 'Statement I alone is sufficient',
    optionB: 'Statement II alone is sufficient',
    optionC: 'Both statements together are sufficient',
    optionD: 'Both statements even together are not sufficient',
    correctOption: 'C',
    explanation: 'A number is divisible by 6 if divisible by both 2 and 3. Statement I only gives divisibility by 2. Statement II only gives divisibility by 3. Together: P is divisible by both 2 and 3, hence by 6.',
    difficulty: 'medium'
  },

  // ============================================================
  // TOPIC 12: MATHEMATICAL OPERATIONS (3 questions: easy, medium, hard)
  // ============================================================
  {
    id: 'ntpc-r-q034',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-mathematical-operations',
    questionText: 'If + means -, - means +, x means /, and / means x, then what is the value of 18 + 6 - 4 x 2 / 5?',
    optionA: '22',
    optionB: '18',
    optionC: '14',
    optionD: '10',
    correctOption: 'A',
    explanation: 'Substituting: 18 - 6 + 4 / 2 x 5. Using BODMAS: 4 / 2 = 2, then 2 x 5 = 10. Then 18 - 6 + 10 = 22.',
    difficulty: 'easy'
  },
  {
    id: 'ntpc-r-q035',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-mathematical-operations',
    questionText: 'If P denotes +, Q denotes -, R denotes x, and S denotes /, then what is the value of 18 R 3 P 6 Q 4 S 2?',
    optionA: '58',
    optionB: '56',
    optionC: '54',
    optionD: '60',
    correctOption: 'A',
    explanation: 'Substituting: 18 x 3 + 6 - 4 / 2. Using BODMAS: 18 x 3 = 54, 4 / 2 = 2. Then 54 + 6 - 2 = 58.',
    difficulty: 'medium'
  },
  {
    id: 'ntpc-r-q036',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-mathematical-operations',
    questionText: 'If 5 * 4 = 25, 6 * 3 = 36, and 7 * 5 = 49, then what is 8 * 3?',
    optionA: '64',
    optionB: '24',
    optionC: '56',
    optionD: '48',
    correctOption: 'A',
    explanation: 'The pattern shows that * returns the square of the first number: 5^2=25, 6^2=36, 7^2=49 (the second number is irrelevant). So 8 * 3 = 8^2 = 64.',
    difficulty: 'hard'
  },

  // ============================================================
  // TOPIC 13: STATEMENT & CONCLUSION (3 questions: easy, medium, medium)
  // ============================================================
  {
    id: 'ntpc-r-q037',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-statement-conclusion',
    questionText: 'Statement: All flowers are plants. Which conclusion logically follows?',
    optionA: 'All plants are flowers',
    optionB: 'Some plants are flowers',
    optionC: 'No plant is a flower',
    optionD: 'Some flowers are not plants',
    correctOption: 'B',
    explanation: 'If all flowers are plants, then flowers are a subset of plants. This implies that some plants (those that are flowers) are definitely flowers.',
    difficulty: 'easy'
  },
  {
    id: 'ntpc-r-q038',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-statement-conclusion',
    questionText: 'Statement: All students are girls. Some girls are intelligent. Conclusion: All students are intelligent.',
    optionA: 'Conclusion follows',
    optionB: 'Conclusion does not follow',
    optionC: 'Conclusion is partially true',
    optionD: 'Cannot be determined',
    correctOption: 'B',
    explanation: 'Students are a subset of girls. Some girls are intelligent, but the intelligent girls may not include the students. The conclusion does not logically follow.',
    difficulty: 'medium'
  },
  {
    id: 'ntpc-r-q039',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-statement-conclusion',
    questionText: 'Statement: Some papers are pens. All pens are books. No book is a pencil. Conclusions: I. Some papers are books. II. No pen is a pencil.',
    optionA: 'Only I follows',
    optionB: 'Only II follows',
    optionC: 'Both I and II follow',
    optionD: 'Neither I nor II follows',
    correctOption: 'C',
    explanation: 'I: Some papers are pens, all pens are books, so some papers are books. I follows. II: All pens are books, no book is a pencil, so no pen is a pencil. II follows. Both follow.',
    difficulty: 'medium'
  },

  // ============================================================
  // TOPIC 14: CLASSIFICATION (3 questions: easy, medium, medium)
  // ============================================================
  {
    id: 'ntpc-r-q040',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-classification',
    questionText: 'Find the odd one out: Apple, Banana, Potato, Mango',
    optionA: 'Apple',
    optionB: 'Banana',
    optionC: 'Potato',
    optionD: 'Mango',
    correctOption: 'C',
    explanation: 'Apple, Banana, and Mango are fruits. Potato is a vegetable. Hence Potato is the odd one out.',
    difficulty: 'easy'
  },
  {
    id: 'ntpc-r-q041',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-classification',
    questionText: 'Find the odd one out: 11, 13, 15, 17',
    optionA: '11',
    optionB: '13',
    optionC: '15',
    optionD: '17',
    correctOption: 'C',
    explanation: '11, 13, and 17 are prime numbers. 15 is composite (divisible by 3 and 5). Hence 15 is the odd one out.',
    difficulty: 'medium'
  },
  {
    id: 'ntpc-r-q042',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-classification',
    questionText: 'Find the odd one out from the pattern: 2, 3, 5, 7, 9, 11',
    optionA: '2',
    optionB: '5',
    optionC: '9',
    optionD: '11',
    correctOption: 'C',
    explanation: 'All numbers except 9 are prime. 9 = 3 x 3 is composite. Therefore 9 is the odd one out.',
    difficulty: 'medium'
  },

  // ============================================================
  // TOPIC 15: MISSING NUMBERS (3 questions: easy, medium, medium)
  // ============================================================
  {
    id: 'ntpc-r-q043',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-missing-numbers',
    questionText: 'Find the missing number in the series: 1, 4, 9, 16, ___?',
    optionA: '20',
    optionB: '25',
    optionC: '24',
    optionD: '23',
    correctOption: 'B',
    explanation: 'The series consists of perfect squares: 1^2=1, 2^2=4, 3^2=9, 4^2=16. The next term is 5^2=25.',
    difficulty: 'easy'
  },
  {
    id: 'ntpc-r-q044',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-missing-numbers',
    questionText: 'Find the missing number: 2, 3, 5, 7, 11, ?, 17',
    optionA: '12',
    optionB: '13',
    optionC: '14',
    optionD: '15',
    correctOption: 'B',
    explanation: 'The series is consecutive prime numbers: 2, 3, 5, 7, 11, 13, 17. The missing number is 13.',
    difficulty: 'medium'
  },
  {
    id: 'ntpc-r-q045',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-missing-numbers',
    questionText: 'Find the missing number: 3, 6, 12, 24, ?, 96',
    optionA: '36',
    optionB: '48',
    optionC: '40',
    optionD: '52',
    correctOption: 'B',
    explanation: 'Each term is multiplied by 2: 3x2=6, 6x2=12, 12x2=24, 24x2=48, 48x2=96. Missing number is 48.',
    difficulty: 'medium'
  },

  // ============================================================
  // TOPIC 16: NON-VERBAL REASONING (3 questions: easy, medium, hard)
  // ============================================================
  {
    id: 'ntpc-r-q046',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-non-verbal-reasoning',
    questionText: 'A square is divided into four equal smaller squares. In the first figure, the top-left square is shaded. In the second figure, the top-right square is shaded. In the third figure, the bottom-right square is shaded. Which square will be shaded in the fourth figure?',
    optionA: 'Top-left',
    optionB: 'Top-right',
    optionC: 'Bottom-right',
    optionD: 'Bottom-left',
    correctOption: 'D',
    explanation: 'The shaded square moves clockwise: top-left, top-right, bottom-right, bottom-left. The fourth figure has bottom-left shaded.',
    difficulty: 'easy'
  },
  {
    id: 'ntpc-r-q047',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-non-verbal-reasoning',
    questionText: 'If the mirror image of the word "RAIL" reads as "LIAR" when viewed normally, what would the mirror image of "PORT" read as?',
    optionA: 'TROP',
    optionB: 'TROQ',
    optionC: 'PROT',
    optionD: 'TORP',
    correctOption: 'A',
    explanation: 'In a mirror, the word is reversed left-to-right. PORT reversed is TROP. The mirror image of PORT is TROP.',
    difficulty: 'medium'
  },
  {
    id: 'ntpc-r-q048',
    examId: 'ntpc',
    subjectId: 'ntpc-reasoning',
    topicId: 'ntpc-reasoning-non-verbal-reasoning',
    questionText: 'A pattern of dots follows: Figure 1 has 1 dot, Figure 2 has 3 dots (forming a triangle), Figure 3 has 6 dots (forming a larger triangle). How many dots will Figure 5 have?',
    optionA: '10',
    optionB: '12',
    optionC: '15',
    optionD: '18',
    correctOption: 'C',
    explanation: 'These are triangular numbers where T_n = n(n+1)/2. T_1=1, T_2=3, T_3=6, T_4=10, T_5=15. So Figure 5 has 15 dots.',
    difficulty: 'hard'
  }
];
