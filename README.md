## What is Delayed Auditory Feedback (DAF)?
- Delayed Auditory Feedback is a type of experiment where participants hear their own voice with a slight delay while they are speaking
- This feedback loop can cause disruptions in speech production, such as stuttering, speaking more slowly, or changing the pitch of their voice
- DAF is commonly used in research to understand how auditory feedback influences speech production and how the brain adjusts to unexpected delays

## What DAF experiment
- How the brain processes feedback from the voice when it is delayed
- How speech production is affected when feedback does not match what the speaker expects to hear in real-time
- What changes occur in neural activity (e.g., EEG signals) when participants experience this delayed feedback
  
## Features
- audioEnvelope
  - a feature that represents the overall loudness or intensity of the sound over time
  - It smooths out the audio waveform to show how the volume changes as the person speaks. For example, when someone speaks loudly, the envelope will rise, and when they speak softly, it will fall
- audioOnsets
  - The audio onsets refer to the starting points of sounds. Whenever a new sound begins (such as when a person starts a word or syllable), an onset is detected
- eggEnvelope
    - the overall activity of the vocal folds during speech
    - It’s similar to the audio envelope but focuses on the actual physical movement of the vocal cords as a person speaks
    - EGG is used to measure how the vocal folds open and close when producing speech, and the envelope represents the strength or intensity of this activity over time
  - eggOnsets

## potential suggestions and findings
- Neural Synchronization Hypothesis
  - Increased phase synchronization in the gamma band (30-80 Hz) between auditory and motor cortices will positively correlate with participants' ability to maintain fluent speech under DAF conditions
- Cognitive Load and Frontal Theta Hypothesis
  - The magnitude of frontal theta activity (4-7 Hz) during DAF will predict the degree of speech disfluency, reflecting increased cognitive effort to maintain speech production
- Auditory Cortex Adaptation Hypothesis
  - The amplitude of the N1/P2 components in auditory event-related potentials will increase with longer DAF delays, indicating heightened attention and processing of the altered feedback
- Motor Cortex Compensation Hypothesis
  - Beta band (13-30 Hz) power over the motor cortex will show a greater decrease during DAF compared to normal feedback, reflecting increased motor planning and execution effort
- Mismatch Negativity (MMN) and Feedback Delay Hypothesis
  - The latency of the Mismatch Negativity (MMN) response will increase proportionally with the length of the auditory feedback delay, indicating a direct relationship between delay time and auditory prediction error processing.
- Temporal Response Function (TRF) Adaptation Hypothesis
  - The peak latency in Temporal Response Functions derived from EEG data will shift in proportion to the DAF delay, reflecting the brain's temporal adaptation to altered feedback
- Individual Differences in DAF Susceptibility Hypothesis
  - Participants with higher baseline alpha power (8-12 Hz) in frontal regions will show greater resilience to DAF effects, as measured by maintained speech fluency and reduced ERP changes
- Emotion Regulation and Prefrontal Activity Hypothesis
  - Increased prefrontal alpha asymmetry during DAF tasks will correlate with lower reported frustration levels, indicating more effective emotion regulation in the face of speech disruption

## EVENT DATA DESCRIPTION
1. audio_envelope_filters_path (audioEnvelopeFilters_ave.fif.gz)
   1. Description: This file likely contains the filters that are applied to the EEG data to extract the temporal response function (TRF) related to the audio envelope.
   2. Audio Envelope: Represents the overall loudness or intensity of the sound over time. The filter is trained to identify how changes in this envelope over time relate to brain activity.
   3. Purpose: By applying these filters, the analysis can reveal how the brain's response fluctuates based on the intensity or volume of auditory stimuli.
2. audio_envelope_patterns_path (audioEnvelopePatterns_ave.fif.gz)
   1. Description: This file likely stores patterns or templates derived from the TRF analysis for the audio envelope.
   2. Purpose: The patterns represent how the brain consistently reacts to changes in audio intensity over time, forming the basis for understanding how well the brain encodes auditory stimuli.
3. audio_onset_filters_path (audioOnsetsFilters_ave.fif.gz)
   1. Description: This file likely contains the filters applied to the EEG data to model brain responses to the audio onsets (the starting points of sound events).
   2. Audio Onsets: The moments when new sounds begin (e.g., at the start of a word or syllable).
   3. Purpose: The filter helps analyze how the brain responds to the onset of sounds, which is critical for understanding speech production under delayed auditory feedback.
4. audio_onset_patterns_path (audioOnsetsPatterns_ave.fif.gz)
   1. Description: This file probably contains patterns generated from the TRF analysis that represent how the brain responds to the onsets of audio signals.
   2. Purpose: These patterns help reveal how the brain consistently reacts when new sounds begin, aiding in the study of auditory processing under DAF conditions.
5. egg_envelope_filters_path (eggEnvelopeFilters_ave.fif.gz)
   1. Description: This file contains filters related to the electroglottography (EGG) envelope. EGG measures the physical activity of the vocal folds.
   2. EGG Envelope: Represents the activity or intensity of the vocal folds during speech production.
   3. Purpose: This filter helps analyze how the brain's response relates to the physical movement of the vocal folds as people speak.
6. egg_envelope_patterns_path (eggEnvelopePatterns_ave.fif.gz)
   1. Description: This file contains the patterns related to the EGG envelope.
   2. Purpose: These patterns likely represent how brain activity correlates with vocal fold movements over time, which is important for understanding speech production mechanisms during DAF.
7. eeg_onset_filters_path (eegOnsetsFilters_ave.fif.gz)
   1. Description: This file contains filters related to EEG onsets, which likely refer to the onset of changes in EEG activity.
   2. Purpose: The file contains filters used to analyze brain responses to the onset of neural events or changes in brain activity.
8. eeg_onset_patterns_path (eegOnsetsPatterns_ave.fif.gz)
   1. Description: This file contains patterns derived from EEG data related to onsets of neural activity or events.
   2. Purpose: These patterns represent how the brain responds to neural onsets, providing insight into brain dynamics during auditory tasks like DAF.
