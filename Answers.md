### Part C – Short Answer (Reasoning)

**1. If you only had 200 labeled replies, how would you improve the model without collecting thousands more?**  
I would leverage data-efficient techniques like few-shot or transfer learning using a pre-trained language model. Additionally, I could use data augmentation strategies, such as paraphrasing existing replies, to expand the dataset while retaining the underlying intent. This way, the model can learn more patterns without needing thousands of new labeled samples.

**2. How would you ensure your reply classifier doesn’t produce biased or unsafe outputs in production?**  
I would carefully curate and audit training data for biased content and continuously test the model against edge cases for safety. Implementing a moderation layer or safety filter, combined with monitoring user feedback, helps catch and mitigate harmful outputs while maintaining user trust.

**3. Suppose you want to generate personalized cold email openers using an LLM. What prompt design strategies would you use to keep outputs relevant and non-generic?**  
I would include key personal or contextual information in the prompt, such as the recipient’s role, company, or recent achievements, and explicitly instruct the model to avoid generic phrases. Framing prompts as if writing a thoughtful, human-to-human message encourages the model to produce more authentic and engaging openers.
