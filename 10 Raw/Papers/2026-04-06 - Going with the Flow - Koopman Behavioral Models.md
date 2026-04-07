---
type: raw_source
source_kind: paper
capture_status: needs_compile
captured: 2026-04-06
source_path: 07 Resources/Papers/835_Going_with_the_Flow_Koopma.pdf
source_url: 
repo_url: 
compiled_note: [[05 Knowledge/Compiled/Going with the Flow - Koopman Behavioral Models]]
tags:
  - raw
  - paper
compiled_on: 2026-04-07
concept_notes:
  - [[05 Knowledge/Concepts/Going with the Flow]]
  - [[05 Knowledge/Concepts/Koopman Behavioral Models]]
compile_quality: failed
compile_failures:
  - deterministic fallback is draft-only; rerun with a real LLM compiler
---

# Going with the Flow - Koopman Behavioral Models

## Source

- Original file: `07 Resources/Papers/835_Going_with_the_Flow_Koopma.pdf`
- Why keep this:

## Raw Markdown

Going with the Flow: Koopman Behavioral Models
as Implicit Planners for Visuo-Motor Dexterity
Author Names Omitted for Anonymous Review. Paper-ID [xxx]
Abstract—There has been rapid and dramatic progress in
robots’ ability to learn complex visuo-motor manipulation skills
from demonstrations, thanks in part to expressive policy classes
that employ diffusion- and transformer-based backbones. How-
ever, these design choices require significant data and compu-
tational resources and remain far from reliable, particularly
within the context of multi-fingered dexterous manipulation.
Fundamentally, they model skills as reactive mappings and rely
on fixed-horizon action chunking to mitigate jitter, creating a
rigid trade-off between temporal coherence and reactivity. In
this work, we introduce Unified Behavioral Models (UBMs) , a
framework that learns to represent dexterous skills as coupled
dynamical systems that capture how visual features of the
environment (visual flow) and proprioceptive states of the robot
(action flow) co-evolve. By capturing such behavioral dynamics ,
UBMs can ensure temporal coherence by construction rather
than by heuristic averaging. To operationalize these models,
we propose Koopman-UBM, a first instantiation of UBMs that
leverages Koopman Operator theory to effectively learn a unified
representation in which the joint flow of latent visual and
proprioceptive features is governed by a structured linear system.
We demonstrate that Koopman-UBM can be viewed as animplicit
planner: given an initial condition, it analytically computes the
desired robot behavior while simultaneously “imagining” the
resulting flow of visual features over the entire skill horizon.
To enable reactivity and adaptation, we introduce an online
replanning strategy in which the model acts as its own runtime
monitor that automatically triggers replanning when predicted
and observed visual flow diverge beyond a threshold. Across seven
simulated tasks and two real-world tasks, we demonstrate that
K-UBM matches or exceeds the performance of state-of-the-art
baselines, while offering considerably faster inference, smooth
execution, robustness to occlusions, and flexible replanning.
I. I NTRODUCTION
Reliable dexterous manipulation with multi-fingered hands
has the potential to enable robots to seamlessly operate in
a world made for and by humans. Unlike simple pick-and-
place with parallel-jaw grippers, multi-fingered dexterity re-
quires mastering high-dimensional coordinated control under
complex contact dynamics, partial observability, and frequent
visual occlusion [1, 2]. Data-driven approaches like Diffu-
sion Policies [3, 4] and Transformers (e.g., ACT [5]) have
revolutionized this space by learning directly from visual
demonstrations. Fundamentally, these approaches model skills
as reactive mappings (ot → at), treating the task as a sequence
of independent decisions rather than a continuous physical
process. To encourage temporal coherence and prevent jitter,
these methods rely heavily on action chunking ( ot → at:t+H)
or temporal ensembling [5, 6] as heuristics that average
predictions over fixed, hard-coded time windows. While ef-
fective, these strategies introduce a rigid trade-off between
deliberate planning (full-horizon predictions) and reactivity
(short chunks), and any resulting coherence is a byproduct of
averaging rather than a fundamental property of the learned
representation (see Fig. 1, Panel A).
An alternative perspective is to view any dexterous skill
not as a sequence of decisions, but as being governed by
an underlying dynamical system . Seminal work on Dynamic
Movement Primitives (DMPs) [7, 8] and numerous dynamical
systems-based approaches [9–13] have long considered skills
as solutions to fictitious dynamical systems. However, they
tend to only model the dynamics of the robot’s movement,
treating the environment as a static boundary condition. While
highly effective for goal-reaching movements, this robot-
centric view fails to capture the essence of dexterous ma-
nipulation: dexterity resides in the intricate coupling between
the robot hand and the environment. In dexterous tasks, the
object’s movement is equally if not more important than that
of the robot.
In this work, we introduce Unified Behavioral Models
(UBMs), a framework that learns to represent dexterous skills
as coupled dynamical systems directly from demonstrations
(see Fig. 1, Panel B). UBMs capture the robot-environment
interdependence by learning the behavioral dynamics of the
entire system that governs how visual features of the envi-
ronment ( visual flow ) and proprioceptive states of the robot
(action flow ) co-evolve. Specifically, UBMs learn a unified
latent space in which the joint state of the robot and object
evolves according to a latent dynamical system. During in-
ference, UBMs can be seen as “Implicit Planners” that can
generate complete “plans” via open-loop latent rollout from
any given initial condition. Crucially, UBMs can trivially
support dynamic chunking as one can flexibly vary the number
of time steps for which the model is rolled out (i.e., a
tunable planning horizon). However, realizing UBMs presents
a significant practical challenge: the joint dynamics of a multi-
fingered hand interacting with a deformable or sliding object
are highly nonlinear and difficult to learn directly from limited
visual data without drifting or diverging.
To overcome the challenges of realizing UBMs, we in-
troduce Koopman-UBM as the first instantiation of UBMs
that leverages Koopman Operator theory [14, 15] to ensure
tractable learning and efficient computation (see Fig. 1, Panel
C). By lifting the nonlinear interaction between the robot and
visual features into a latent space where their joint evolution
becomes linear ( zt+1 = Kz t), Koopman-UBM transforms
the complex nonlinear dynamics learning problem into a
representation learning problem for linear dynamics. After

Fig. 1: (A) Standard reactive policies (e.g., Diffusion, ACT) map observations to short-horizon action chunks, lacking a consistent internal
model of the future or memory beyond the observation window, leading to temporal incoherence and hand-coded chunk lengths. (B) In
contrast, Unified Behavioral Models (UBM) model skills as joint behavioral dynamics of the robot and environment governing a continuous
flow in a latent space, ensuring coherence and enabling full-horizon “planning” from initial conditions. (C) We propose Koopman-UBM
as the first instantiation of UBMs, which lifts visual and proprioceptive observations into a latent space governed by a learned Koopman
Operator. By enforcing linear spectral dynamics ( zt+1 = Kz t) over a unified “state-inclusive” latent space, K-UBM ensures enables fast
inference and predictive monitoring. (D) Our approach enables temporally-coherent predictions (dashed-purple) that are robust to visual
occlusion (dashed green and purple trajectories inside gray boxes) and reactivity via an event-triggered replanning strategy that reinitializes
the UBM only when the predicted visual features diverge from reality (top orange box).
encoding the initial conditions into the latent space, Koopman-
UBM can generate the entire nominal trajectory via linear
rollout, ensuring temporal coherence by construction regard-
less of the rollout horizon. This allows Koopman-UBM to
act as an implicit visuo-motor planner that predicts the future
flow of the environment (e.g., object motion) alongside the
robot’s actions without the computational cost of continuous
sequential decision making via reactive mapping.
To ground K-UBM in raw high-dimensional visual data,
We fuse proprioceptive history with robust visual representa-
tions, and investigate the effectiveness of two complementary
representations: (i) motion-centric features derived from point
tracking (Object Flow [16]), and (ii) manipulation-centric fea-
tures learned via self-supervised (Dynamo [17]). In addition,
we leverage a state-inclusive lifting strategy (i.e., visual and
proprioceptive features appear as a subvector ofz [18]) to form
a latent state that explicitly embeds the system’s interpretable
physical configuration and enable fast decoder-free inference.
By optimizing this representation jointly with the behavioral
dynamics, our method learns dynamics-aware embeddings that
linearize complex contact behaviors. This helps ensure that
Koopman-UBM’s roll-outs are reliable and coherent during
nominal execution. Unlike reactive policies that falter and
freeze during strong occlusions and frame drops, K-UBM
can faithfully propagate the system’s “momentum” without
sensory feedback by relying on its internal dynamics model
to bridge perceptual gaps (see Fig. 1, Panel D).
However, relying solely on open-loop rollout from an initial
conditions has a considerable limitation: it cannot account
for unanticipated external disturbances during execution. To
enable reactivity, we leverage UBM’s unique ability to predict
visual features to introduce a framework-level event-triggered
replanning strategy. Because Koopman-UBM can explicitly
predict the nominal flow of visual features, the model can
act as its own runtime monitor (see Fig. 1, Panel D). Our
replanning strategy monitors the error between predicted and
observed visual features. The system executes the initial
nominal plan as long as predictions match reality; when a
disturbance causes the error to exceed a threshold, the system
triggers a replan (re-initializes zt and computes a new coherent
trajectory). Combining this flexible replanning strategy with
Koopman-UBM allows the robot to flexibly navigate the
spectrum between deliberate planning and reactive decision
making without enforcing a rigid trade-off.
In summary, our key contributions are:
1) We introduce Unified Behavioral Models (UBM) , a
class of sensory-motor skill models that encode dexter-
ous skills as coupled dynamical systems, capturing the
inter-dependence of robot actions and environmental fea-
tures. UBMs ensure temporal coherence by construction
and enable full-horizon predictions of unified nominal
actions and visual feature flows.
2) We propose Koopman-UBM, a Koopman-based instan-
tiation of UBM that acts as an implicit visuo-motor
planner. By leveraging state-inclusive lifting and lin-
ear spectral dynamics, Koopman-UBM enables reliable
open-loop trajectory generation while also supporting
closed-loop reactivity via predictive monitoring.
3) We provide a comprehensive evaluation across 7 sim-
ulated and 4 real-world dexterous manipulation tasks,

demonstrating that our UBM-based approach matches
or exceeds the performance of state-of-the-art baselines
(e.g., Diffusion policy, ACT, etc.), while offering con-
siderably faster inference, smooth execution, robustness
to occlusions, and flexible replanning.
II. U NIFIED BEHAVIORAL MODELS
We begin by formulating the problem of learning visuo-
motor dexterous skills from demonstrations, and introduce the
notion of unified behavioral models (UBMs).
Let D = [{o(1)
t , a(1)
t }T (1)
t=1 , · · · , {o(N )
t , a(N )
t }T (N )
t=1 ] denotes a
dataset of N demonstrations of a certain target skill (e.g.,
opening a box, hammering a nail, etc.), with the i-th demo
being a trajectory with T (i) steps. At each time step t, the
observation ot consists of the robot joint state and visual
observations, while the action at corresponds to the robot
joint command. Specifically, we define the observation as
ot = {qt, It}, where qt ∈ Q ⊆ Rdq denotes the robot
joint state (i.e., joint configuration of the arm and the hand)
with dq degrees-of-freedom (dof), and It ∈ I ⊆ RH×W ×3
denotes the RGB visual observation. The action is defined as
at = q target
t ∈ Q ⊆ Rdq, representing the robot commands
issued to the low-level controller.
The most common approach to learning the dexterous skill
encoded in D involves learning a reactive policy [3, 5]. A
reactive policy can be represented as a map π : o t 7→ at
(or more generally, ot−h:t 7→ at:t+l), where h = H ∈ N and
l = L ∈ N denote the hard-coded, fixed lengths of history and
action chunks, respectively.
In contrast to reactive policies, we take the approach of
learning a unified behavioral model (UBM) D. Instead of
building a map from observations to action (chunks), UBMs
learn to represent the target dexterous skill as a dynamical
system that encodes behavioral dynamics: laws that govern
how visual features of the environment (visual flow) and
proprioceptive states of the robot (action flow) co-evolve.
Formally, a UBM can be defined as zt+1 = fU BM(zt), where
zt = fenc(ξt) is the latent state of the UBM produced by
encoding the unified behavioral state ξt = [at, ot], containing
both action and observation information. In order to extract
the predicted actions from the latent flow, UBMs also require
an action decoder: at = fdec(zt). As such learning a UBM
requires the learning fU BM (the latent behavioral dynamics
model), fenc (unified sensory-motor encoder), and fenc (action
decoder) simultaneously. While it might be possible to learn
these modules separately, co-training them is necessary to
learn a temporally-coherent and predictive latent representa-
tion over which we could learn dynamics [19, 20]. Although
closely related, note that UBMs are different from the increas-
ingly popular notion of “robotic world models” [21, 22]. While
world models learn to predict the impact of a given action by
approximating the underlying natural dynamics of the system
(i.e., xt+1 = fW M(xt, at) where xt is the (latent) state of
interest), UBMs capture the coupled sensory-motor behavioral
dynamics.
Given the above formulation, UBMs offer a number of
practical benefits when learning dexterous skills. First, they
serve as implicit planners capable of generating “plans” of
arbitrary lengths up to the full skill horizon. Specifically, given
an initial condition ξ0 = [a0, o0], we can initialize the unified
latent state z0 = fenc(ξ0) and forward propagate (rollout) the
learned dynamics fU BM(·) up to any desired number of time
steps Tl ≤ TH (with TH as the full skill-horizon) to generate
{zt}Tl
t=1. Finally, we can leverage the learned action decoder
fdec(·) to extract the corresponding action trajectory {at}Tl
t=1.
In addition, to ensure inference-time accessibility of the ini-
tial state, we add auxiliary initial state to the action trajectories.
Details are provided in the appendix. VII.
III. K OOPMAN -BASED UNIFIED BEHAVIOR MODELS
While the above formulation of UBMs is easy to describe,
learning them can present numerous changes. In particular,
high-dimensional raw visual observations and action spaces,
noisy data collection, non-smooth contact dynamics, temporal
drift in latent dynamical systems can introduce considerable
challenges and require careful considerations. In this sec-
tion, we introduce Koopman-UBM, a practical instantiation of
UBMs that leverages Koopman operator theory and motion-
centric visual features to overcome these challenges.
Koopman-UBM combines representation learning and latent
behavioral dynamics learning, and learns from demonstrations
in two stages: (i) Visual Feature Extraction , which extracts
motion-centric visual features from raw images {It} across
all time steps of the demonstrations (See Section. III-A), and
ii) Koopman-UBM Learning : learn a Koopman-based UBM
that can predicts both visual feature and action flows given
initial conditions (See Section. III-B).
A. Extracting Visual Features
In this section, we briefly describe the frameworks for
extracting and compressing relevant visual features from RGB
images. Without the crucial compression step, UBMs would
attempt to learn the dynamics of task-irrelevant pixel-level in-
formation and potentially find spurious correlations or struggle
to converge. In this work, we investigate two visual representa-
tions: i) object flow point features [16], and ii) DynaMo visual
features [17]. See Appendix. VIII for detailed implementation
of these two visual feature extracting frameworks.
Object Flow Points : We track 256 points using SAM3
and CoTracker, then compress their coordinates into a 128-
dimensional latent space using a convolutional autoencoder to
provide a compact, motion-centric representation.
DynaMo: We utilize a ResNet-18 encoder trained with
a self-supervised, dynamics-consistency objective that learns
compact, dynamics-aware embeddings directly from task-
specific RGB observations.
B. Koopman Unified Behavioral Model Learning
In this section, we describe our approach to learning Koop-
man UBMs procedure. Specifically, we learning Koopman
UBMs from demonstrations by jointly training i) a unified

spectral encoder and ii) an approximated Koopman operator
governing the linear evolution in unified latent space.
Defining the unified Behavioral State : We define the unified
behavioral state by concatenating robot action at and learned
visual feature ϕt:
ξt ≜

at
ϕt

∈ Rdϕ .
where dϕ = dq + dϕ is the size of the unified behavioral
state. To balance the magnitudes of the state components, we
rescale the visual features ϕt by a constant factor computed
based on the average l2 norms of the visual features and the
robot actions over all demonstrations.
Unified Spectral Latent: To approximate the Koopman-
invariant subspace, we first define a unified spectral encoder
gθ : ξt 7→ ψt that acts as a lifting function, with θ as its learn-
able parameters. We parametrize this encoder using a multi-
layer perceptron (MLP) that computes the lifted behavioral
state ψt ∈ Rψ from the unified behavioral state ξt. Then,
we define a state-inclusive latent representation of the lifted
behavioral state as
zt ≜

ξt
ψt

∈ Rdz .
where dz = dξ + dψ denotes the dimension of the Koopman-
UBM’s latent space. By explicitly including ξt in the latent
representing, we enable the latent Koopman dynamics to be
grounded in the behavioral states, avoiding drifts ane en-
couranging temporal coherence. Further, state-inclusive latent
representation enable fast decoder-free inference.
Linear Latent Dynamics: With the latent space established,
we can define a learnable Koopman matrix K ∈ Rdz×dz such
that the dynamics in the latent space can be approximated as
zt+1 = K zt.
Co-training the Encoder and Dynamics: To ensure that the
learned latent representation of the unified behavioral state
is dynamics-aware and will permit a linear structure, we co-
train train the linear dynamics jointly with the unified spectral
encoder. We minimize a multi-step latent prediction loss over
a prediction horizon H to encourage temporal coherence in the
latent space and minimize drift. We compute multi-step latent
predictions by repeatedly applying the koopman operator on
a given latent state:
ˆzt+l = K l zt, l = 1, . . . , H
We define our linear coherence loss as the prediction error
against the ground-truth latent targets:
LK-coherence = Et
" HX
l=1


K l zt − zt+l


2
2
#
.
After comprehensive experimentation, we identified two key
factors that influenced training stability:
Learning rates and gradient clipping: We found that training
stability improves significantly when the Koopman matrix is
updated at a slower rate than the unified spectral encoder.
We believe this is because the Koopman matrix is applied
repeatedly during multi-step prediction, and its gradients are
more prone to explosion. As such, we recommend using a
smaller learning rate for the Koopman matrix, along with
gradient clipping.
Identity initialization of the Koopman matrix: We found that
initializing the Koopman matrix K to the identity matrix is
crucial for stability, especially in the early stages of training.
Intuitively, an identity initialization corresponds to be static
latent space and updating the matrix (especially at a slower
rate as noted above) allows the latent dynamics to gradually
grow in a rapidly-evolving latent space (as the encoder learns
at a faster rate).
IV. S IMULATION EVALUATION
A. Experimental Design
Tasks: We consider seven challenging and representative sim-
ulated dexterous manipulation tasks (See Fig. 2 for visual illus-
trations.). Below, we briefly describe each task, and additional
details, including the task state space, objectives, sampling
ranges, and success criteria, can be found in Appendix IX.
Dexart [23]. In the SAPIEN simulator [24], the robot platform
consists of a 6-DoF XArm6 arm and a 16-DoF Allegro hand,
and is required to perform three challenging articulated object
dexterous manipulation tasks:
• Bucket: Lift a randomly positioned bucket using a stable
form-closure grasp [25].
• Laptop: Grasp the center of a randomly placed laptop
screen and open the laptop lid.
• Toilet: Grasp and open the large lid of a randomly placed
toilet.
Adroit [26]. In the MuJuCo simulator [27], the robot platform
consists of an Adroit hand—a 30-DoF system comprising a
24-DoF hand and a 6-DoF floating wrist base, and is required
to perform four representative dexterous manipulation tasks:
• Door opening: Given a randomized door position, undo
the latch and drag the door open.
• Tool use: Pick up the hammer to drive the nail into the
board placed at a randomized height.
• In-hand reorientation: Reorient the blue pen to a random-
ized goal orientation (green pen).
• Object relocation: Move the blue ball to a randomized
target location (green sphere).
Note that Tool use, In-hand reorientation, and Object reloca-
tion are goal-conditioned tasks.
Demonstrations: For DexArt tasks, we collect 30 demonstra-
tions for training and 30 for testing. For Adroit tasks, we
collect 50 demonstrations for training and 30 for testing. For
both simulation tasks, we use the pre-trained RL experts. Each
demonstration consists of visual observations, robot states, and
commanded actions.
Baselines: We choose the following baselines:
General methods: We consider two commonly used visuomo-
tor learning approaches:
• Diffusion policy [3]: Diffusion policy formulates visuo-
motor robot policies as Denoising Diffusion Probabilistic

Door opening
Bucket Laptop Toilet
Tool use In-hand reorientation Relocation
DexArt Tasks
Adroit Tasks
Uncover Pot Open Lid
Real-world Tasks
Fig. 2: We evaluate K-UBM on seven simulations tasks and two real-world tasks.
Models, which learns to produce robot action trajecto-
ries by iteratively refining random noise into a specific
motion, conditioned on observations.
• Action Chunking Transformer (ACT) [5]: ACT is trained
to predict the sequence of future actions given the cur-
rent observations. It handles the variability of human
demonstrations by leveraging a Conditional Variational
Autoencoder (CV AE).
Existing Koopman-based approaches: We consider two exist-
ing Koopman-based methods that support learning from visual
features:
• KODex [28]: Uses predefined polynomial lifting func-
tions, allowing closed-form least-squares one-step predic-
tion, but does not leverage multi-step prediction loss.
• KOROL [29]: Uses only the multi-step robot action
prediction loss to enable learning visual features from
images, but does not provide supervision for visual fea-
ture prediction.
B. General Task Performance Evaluation
In this section, we evaluate policy performance on seven
simulated tasks and four real-world tasks. We compare all
baselines using two types of visual features in terms of task
success rate and inference cost.
We undertook several precautions to ensure a fair compari-
son. First, we designed the robot state and visual features for
all methods to be identical. Second, we carefully designed the
baselines policies and tuned their hyper-parameters for each
baseline method (Appendices XI and XII). Third, we trained
each method policy over five random seeds to control for
initialization effects [30], except for KODex, which computes
an analytical solution. Note that for real-world tasks, due to
Method Inference Time (ms,↓)
Flow DynaMo
Diffusion 29.95(±1.37) 36.31(±2.29)
ACT 0.52( ±0.06) 0.29( ±0.02)
KOROL 0.41(±0.07) 0.36(±0.04)
KODex 0.40( ±0.04) 0.37( ±0.04)
K-UBM 0.42(±0.05) 0.47( ±0.14)
TABLE I: Average per-step inference time of each method, excluding
visual feature extraction time. Koopman-based policies and ACT are
orders of magnitude faster than diffusion policies.
the burden of physical evaluation, we train and evaluate each
policy on a single random seed.
In Fig. 3, we report task success rates on unseen test sets.
On average, our K-UBM method achieves the highest mean
success rate. We also observe that diffusion- and ACT-based
policies require task-specific tuning of the action chunk size.
This observation is consistent with the practical challenges of
architecture tuning for these models.
We also evaluate the inference cost of each method for the
bucket task1. We report the inference cost in policy query time,
which measures only the time required for policy inference,
i.e., the total time the policy spends generating trajectories for
task execution. The timing result is averaged over the total
number of time steps, as different policies complete the task
at different horizons.
From the results in Table. I, we can clearly observe the
advantages of the flow-based policies. Since they do not rely
heavily on real-time feedback, the burden of online visual
processing is substantially reduced, leading to significantly
faster policy rollouts.
1The inference cost is similar across tasks, so we report results on a single
representative task for brevity.

FlowDynaMo
Fig. 3: We report the task success rates for each method on the test sets using both visual features (Flow on the top row and DynaMo on
the bottom row). For baseline methods, error bars indicate the standard deviation over five random seeds.
C. Enabling Reliable Evolution of Robot States and
Manipulation-Centric Environment Dynamics
A major benefit of our method is the joint prediction
of both robot states and manipulation-centric environment
dynamics. The accuracy of robot state prediction has already
been demonstrated in the previous section through task per-
formance. In this section, we evaluate the prediction accuracy
of manipulation-centric environment dynamics, which can be
utilized in multiple ways, such as triggering replanning (see
Section IV-D), serving as an inference-time verification signal
(see result discussion of this section), or acting as an object-
centric tracking reward for reinforcement learning [31]. Since
Diffusion, ACT, and KOROL do not support explicit object
prediction, and KODex performs significantly worse as shown
in Section IV-B, we do not include comparisons with these
baseline methods.
Flow Feature Prediction First, in Fig. 4, we present qualita-
tive results for three reconstructed flow point trajectories on
the test set for the Bucket, Door, and Relocate tasks. These tra-
jectories are obtained by decoding the flow features predicted
via Koopman rollouts using the flow decoder learned during
autoencoder training. We further visualize the reconstructed
flow points by overlaying them on the corresponding images
as red dots. From these results, we can see that the predicted
flow features effectively capture and reflect the manipulation
objectives throughout the entire task execution.
Furthermore, we evaluate the quantitative prediction quality
of the reconstructed flow points. In Fig. 6 (top row), we report
the root mean square error (RMSE) between the predicted
and ground-truth flow points over time for all seven simula-
tion tasks on the test sets, averaged across all test rollouts.
Since rollout lengths vary across runs, we visualize the error
using normalized trajectory percentiles. We further separate
the prediction errors for successful and failed rollouts. As
shown in the figure, failed rollouts consistently exhibit larger
flow prediction errors than successful ones, revealing a strong
correlation between degraded object flow prediction and poor
Time
Door
Relocate
 Bucket
Fig. 4: We visualize the predicted flow points by decoding the flow
features and overlaying them on the corresponding images.
Bucket Door
 Relocate
Fig. 5: We visualize the predicted DynaMo features by projecting
them together with the ground-truth features using t-SNE.
robot execution.
Dynamo Feature Prediction For DynaMo features, fol-
lowing an evaluation procedure similar to that used for flow
features, we first present three qualitative results comparing
the predicted and ground-truth DynaMo features in the latent
space using t-SNE [32] visualization, as shown in Fig. 5. From
these results, we observe that the predicted high-dimensional

FlowDynaMo
Bucket Laptop Toilet Door opening Tool use
In-hand reorientation Relocation
Fig. 6: In the top row, we show the reconstruction error between the predicted and ground-truth flow points. In the bottom row, we report
the cosine similarity between the predicted DynaMo features and the ground-truth trajectories.
visual features align well with the ground-truth features.
We then evaluate the cosine similarity between the predicted
and ground-truth features for all seven simulation tasks on
the test sets, averaging the results across all test rollouts and
visualizing them using trajectory percentiles, as shown in the
bottom row of Fig. 6. Overall, we observe that the cosine
similarity generally decreases over time, indicating increasing
prediction error, which is expected for long-horizon predic-
tions. Notably, for the Tool Use and In-Hand Reorientation
tasks, the feature similarity varies only slightly, resulting in
non-monotonic curves.
In addition, although the trend is less pronounced than in
the flow prediction curves, we still observe a similar pattern:
failed rollouts generally exhibit lower cosine similarity than
successful ones.
D. Reactivity Experiments
One potential concern is that our Koopman-based policy
may lack reactivity, as the robot executes actions in a purely
open-loop manner. However, in this section, we illustrate how
our policy can achieve system-level reactivity, rather than pure
policy-level. To demonstrate this, we conduct the reactivity
experiments on the door opening and object relocation tasks,
while comparing against diffusion- and ACT-based policies.
Specifically, during rollouts on the test sets, we change the
handle position for the door opening task by sampling from the
set of positions that are far away from the previously observed
ones. We apply the same procedure to the relocation task:
after grasping, we modify the goal position, thereby requiring
the robot to transport the object to a different target location.
For our policy, we continuously track the visual features and
compute the discrepancy between the predicted ones and those
observed from real-time images. When this error increases
sharply (i.e., changes in the flow centroid position for the flow-
based policy, and cosine similarity variations for the DynaMo-
based policy), a replanning trigger is activated, prompting the
policy to generate a new trajectory for execution, to which
the robot can seamlessly switch. See the top row of Fig. 9 in
Appendix. XIII for two examples of the flow-based policy for
each task, illustrating that when the environment changes, the
resulting increase in prediction error is pronounced and readily
detectable. In the bottom rows, we design the same strategy to
Task Method Success Count
Flow DynaMo
Door Opening K-UBM (Open-loop) 3/30 2/30
K-UBM 22/30 3/30
Relocation
K-UBM (Open-loop) 1/30 1/30
Diffusion 6/30 21/30
ACT 2/30 15/30
K-UBM 15/30 15/30
TABLE II: Success counts under task perturbations for Door Opening
and Relocation. We report the number of successful rollouts out of 30
for flow-based and DynaMo-based policies. We omit the Diffusion
and ACT for the Door Opening since they performs poorly even
without changes.
the DynaMo features, where significant changes in the latent
feature space can similarly serve as replanning triggers.
In Table II, we show the results for both flow policies and
DynaMo policies. We first report the success rates of pure
full-horizon open-loop tracking, i.e., without reacting to task
changes, to highlight the severity of the task perturbations as
evidenced by the extremely low open-loop success rates. We
also report the success rates of the Diffusion and ACT policies
under this setting to demonstrate their ability to react to such
changes. Finally, for our method, we first report the accuracy
of detecting the replanning trigger at the desired reactivity step.
Using the flow-based policy, the trigger is correctly detected in
30/30 test episodes for both tasks. In contrast, due to the subtle
visual changes associated with door position variations, the
DynaMo-based trigger fails to reliably detect the replanning
event, which in turn leads to a lower task success rate.
From the results of task success rates, we observe that
even under challenging environmental changes, the ability
to replan from the beginning provides our framework with
strong reactivity, as evidenced by comparable task success
rates or only a slight degradation. Interestingly, diffusion- and
ACT-based policies also exhibit reactive behavior when using
DynaMo features, but perform extremely poorly with flow
features.
Additionally, we present two qualitative examples for each
task using the flow-based policy to illustrate the replanning
procedure in Fig. 7. These results show that once replanning

Time
DoorRelocate
Replanning triggered
Fig. 7: For both tasks, the left column shows the robot executing
the original trajectory, where green points denote the predicted flow
points and blue points denote the ground-truth flow points. The
middle column illustrates the environment change. Specifically, a new
handle position for the door-opening task and a new goal position
for the relocation task—which leads to a large discrepancy between
the predicted (green) and ground-truth (blue) flow points. The right
column shows the robot following the replanned trajectory, with red
points indicating the new flow points.
is triggered, the framework can reliably detect the change
and seamlessly switch the robot to a replanned trajectory to
successfully complete the updated task.
E. Additional Experiments
In Appendix. XIV, we conduct systematic experiments
evaluating the robustness of reactive policies to camera noise,
highlighting the benefits of reliable prediction under tracking
failures. Additionally, we report ablation experiments on the
Koopman learning recipe in Appendix. XV.
Time
Segmentation Mask (SAM3) Predicted Flow Trajectories
Prompt: “a small grey cloth”
Prompt: “a tool box”
Reveal PotOpen Lid
Fig. 8: Left: we demonstrate the prompts used for SAM3 to generate
object-centric masks. Right: we show the flow predictions produced
by the trained K-UBM and the flow decoder, overlaid on the
manipulation images.
V. R EAL -WORLD EVALUATION
In this section, we demonstration our framework can also
be utilized on the real-world tasks. In the real world, the
robot platform consists of a 7-DoF Kinova arm and the 6-
DoF PSYONIC hand, and is required to perform two different
manipulation tasks: i) Cloth uncovering, and ii) Tool box
opening. See Fig. 2 for an example.
Method Uncovering Box Opening
ACT 4/10 10/10
K-UBM 4/10 8/10
TABLE III: Evaluation results of ACT and K-UBM on two real tasks.
For each task, we collect 15 demonstrations for training
and 10 for testing. Each demonstration consists of visual
observations, robot states, and commanded actions. We choose
Diffusion-based policies, as the baseline.
First, in Fig. 8, we illustrate the prompts used for SAM3
to generate object-centric masks on the left. On the right, we
show the flow predictions produced by the trained Koopman
models and the flow decoder, overlaid on the manipulation
images.
We report real-world task success rates for our method K-
UBM, and compared with the best-performing ACT. As shown
in Table. III, K-UBM performs comparably to ACT.
VI. C ONCLUSIONS , LIMITATIONS AND FUTURE WORK
We introduced Unified Behavioral Models (UBMs), a
framework treating dexterous manipulation as the coupled
evolution of robot and environment dynamics in a shared latent
space. We proposed Koopman-UBM, with several crucial
design choices to enable effective learning visuo-motor be-
havioral dynamics, enabling both temporal coherence and fast
inference. Across seven simulated and two real-world tasks, K-
UBM bridges dynamical systems theory with modern visual
learning, matching state-of-the-art baselines while offering
superior occlusion robustness and event-triggered replanning.
Limitations: While promising, our current instantiation of
UBMs has three primary limitations. First, while K-UBM’s
linear dynamics capture coarse-grained behavior, they smooth
over sharp contact discontinuities; explicit hybrid modeling
(e.g., switching Koopman operators) may be needed for high-
frequency impact tasks. Second, our “implicit planning” via
open-loop rollout might not be sufficient in highly stochastic
environments with unpredictable object’s dynamics are unpre-
dictable and will likely require online adaptation or residual
corrections. Third, our reactivity relies on visual feedback;
simultaneous occlusion and disturbance can delay replanning
and cause failure.
Future Work: The UBM framework opens several exciting
directions for future research. Future work could explore
more expressive architectures for UBM (e.g., Neural ODEs,
Transformers, Diffusion), and incorporate active perception for
robust predictive monitoring and reward signals. Additionally,
integrating UBMs into hierarchical control (in which founda-
tion models, such as VLMs, modulate attractors or switch be-
tween primitives) could enable language-driven, long-horizon
tasks. Ultimately, UBMs provide a promising alternative to
reactive policies, flexibly blending forethought with reflex.

REFERENCES
[1] Lixin Xu, Zixuan Liu, Zhewei Gui, Jingxiang Guo, Zeyu
Jiang, Zhixuan Xu, Chongkai Gao, and Lin Shao. Dexs-
ingrasp: Learning a unified policy for dexterous object
singulation and grasping in cluttered environments. arXiv
preprint arXiv:2504.04516, 2025.
[2] Shan An, Ziyu Meng, Chao Tang, Yuning Zhou, Tengyu
Liu, Fangqiang Ding, Shufang Zhang, Yao Mu, Ran
Song, Wei Zhang, et al. Dexterous manipulation
through imitation learning: A survey. arXiv preprint
arXiv:2504.03515, 2025.
[3] Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau,
Yilun Du, Benjamin Burchfiel, Russ Tedrake, and Shuran
Song. Diffusion policy: Visuomotor policy learning via
action diffusion. The International Journal of Robotics
Research, 44(10-11):1684–1704, 2025.
[4] Moritz Reuss, Maximilian Li, Xiaogang Jia, and Rudolf
Lioutikov. Goal-Conditioned Imitation Learning us-
ing Score-based Diffusion Policies. In Proceedings
of Robotics: Science and Systems , Daegu, Republic of
Korea, 7 2023. doi: 10.15607/RSS.2023.XIX.028.
[5] Tony Zhao, Vikash Kumar, Sergey Levine, and Chelsea
Finn. Learning fine-grained bimanual manipulation with
low-cost hardware. Robotics: Science and Systems XIX ,
2023.
[6] Yuejiang Liu, Jubayer Ibn Hamid, Annie Xie, Yoonho
Lee, Maximilian Du, and Chelsea Finn. Bidirectional
decoding: Improving action chunking via closed-loop
resampling. arXiv preprint arXiv:2408.17355 , 2024.
[7] Auke Jan Ijspeert, Jun Nakanishi, Heiko Hoffmann,
Peter Pastor, and Stefan Schaal. Dynamical movement
primitives: learning attractor models for motor behaviors.
Neural computation, 25(2):328–373, 2013.
[8] Matteo Saveriano, Fares J Abu-Dakka, Alja ˇz Kram-
berger, and Luka Peternel. Dynamic movement prim-
itives in robotics: A tutorial survey. The International
Journal of Robotics Research , 42(13):1133–1184, 2023.
[9] Harish Ravichandar, Athanasios S Polydoros, Sonia
Chernova, and Aude Billard. Recent advances in robot
learning from demonstration. Annual review of control,
robotics, and autonomous systems , 3:297–330, 2020.
[10] S. Mohammad Khansari-Zadeh and Aude Billard. Learn-
ing Stable Nonlinear Dynamical Systems With Gaussian
Mixture Models. IEEE Transactions on Robotics , 27
(5):943–957, October 2011. ISSN 1941-0468. doi:
10.1109/TRO.2011.2159412. Conference Name: IEEE
Transactions on Robotics.
[11] Shikhar Bahl, Mustafa Mukadam, Abhinav Gupta, and
Deepak Pathak. Neural dynamic policies for end-to-end
sensorimotor learning. Advances in Neural Information
Processing Systems, 33:5058–5069, 2020.
[12] Karl Van Wyk, Ankur Handa, Viktor Makoviychuk, Yijie
Guo, Arthur Allshire, and Nathan D Ratliff. Geometric
fabrics: a safe guiding medium for policy learning. In
2024 IEEE International Conference on Robotics and
Automation (ICRA), pages 6537–6543. IEEE, 2024.
[13] Mandy Xie, Karl Van Wyk, Ankur Handa, Stephen Tyree,
Dieter Fox, Harish Ravichandar, and Nathan Ratliff.
Neural Geometric Fabrics: Efficiently Learning High-
Dimensional Policies from Demonstration. In Conference
on Robot Learning (CoRL) , 2022.
[14] B. O. Koopman. Hamiltonian Systems and Transfor-
mation in Hilbert Space. Proceedings of the National
Academy of Sciences , 17(5):315–318, 1931. doi: 10.
1073/pnas.17.5.315.
[15] Alexandre Mauroy, Y Susuki, and Igor Mezi ´c. Koopman
operator in systems and control . Springer, 2020.
[16] Nikita Karaev, Ignacio Rocco, Benjamin Graham, Natalia
Neverova, Andrea Vedaldi, and Christian Rupprecht.
Cotracker: It is better to track together. In European
conference on computer vision , pages 18–35. Springer,
2024.
[17] Zichen Cui, Hengkai Pan, Aadhithya Iyer, Siddhant Hal-
dar, and Lerrel Pinto. Dynamo: In-domain dynamics
pretraining for visuo-motor control. Advances in Neural
Information Processing Systems, 37:33933–33961, 2024.
[18] Milan Korda and Igor Mezi ´c. Linear predictors for
nonlinear dynamical systems: Koopman operator meets
model predictive control. Automatica, 93:149–160, July
2018. ISSN 0005-1098. doi: 10.1016/j.automatica.2018.
03.046. URL https://www.sciencedirect.com/science/
article/pii/S000510981830133X.
[19] Mido Assran, Adrien Bardes, David Fan, Quentin Gar-
rido, Russell Howes, Mojtaba, Komeili, Matthew Muck-
ley, Ammar Rizvi, Claire Roberts, Koustuv Sinha, Artem
Zholus, Sergio Arnaud, Abha Gejji, Ada Martin, Fran-
cois Robert Hogan, Daniel Dugas, Piotr Bojanowski,
Vasil Khalidov, Patrick Labatut, Francisco Massa, Marc
Szafraniec, Kapil Krishnakumar, Yong Li, Xiaodong Ma,
Sarath Chandar, Franziska Meier, Yann LeCun, Michael
Rabbat, and Nicolas Ballas. V-JEPA 2: Self-Supervised
Video Models Enable Understanding, Prediction and
Planning, June 2025. URL http://arxiv.org/abs/2506.
09985. arXiv:2506.09985 [cs].
[20] Quentin Garrido, Tushar Nagarajan, Basile Terver, Nico-
las Ballas, Yann LeCun, and Michael Rabbat. Learning
Latent Action World Models In The Wild, January 2026.
URL http://arxiv.org/abs/2601.05230. arXiv:2601.05230
[cs].
[21] Bo Ai, Stephen Tian, Haochen Shi, Yixuan Wang, To-
bias Pfaff, Cheston Tan, Henrik I. Christensen, Hao
Su, Jiajun Wu, and Yunzhu Li. A review of learning-
based dynamics models for robotic manipulation. Sci-
ence Robotics, 10(106):eadt1497, September 2025. doi:
10.1126/scirobotics.adt1497. URL https://www.science.
org/doi/10.1126/scirobotics.adt1497.
[22] Chenhao Li, Andreas Krause, and Marco Hutter. Robotic
World Model: A Neural Network Simulator for Robust
Policy Optimization in Robotics, April 2025. URL http:
//arxiv.org/abs/2501.10100. arXiv:2501.10100 [cs].
[23] Chen Bao, Helin Xu, Yuzhe Qin, and Xiaolong Wang.

Dexart: Benchmarking generalizable dexterous manipu-
lation with articulated objects. In Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 21190–21200, 2023.
[24] Fanbo Xiang, Yuzhe Qin, Kaichun Mo, Yikuan Xia, Hao
Zhu, Fangchen Liu, Minghua Liu, Hanxiao Jiang, Yifu
Yuan, He Wang, et al. Sapien: A simulated part-based
interactive environment. In Proceedings of the IEEE/CVF
conference on computer vision and pattern recognition ,
pages 11097–11107, 2020.
[25] Antonio Bicchi and Vijay Kumar. Robotic grasping
and contact: A review. In Proceedings 2000 ICRA.
Millennium conference. IEEE international conference
on robotics and automation. Symposia proceedings (Cat.
No. 00CH37065), volume 1, pages 348–353. IEEE, 2000.
[26] Aravind Rajeswaran, Vikash Kumar, Abhishek Gupta,
Giulia Vezzani, John Schulman, Emanuel Todorov, and
Sergey Levine. Learning complex dexterous manipula-
tion with deep reinforcement learning and demonstra-
tions. arXiv preprint arXiv:1709.10087 , 2017.
[27] Todorov, Emanuel and Erez, Tom and Tassa, Yuval.
Mujoco: A physics engine for model-based control. In
2012 IEEE/RSJ International Conference on Intelligent
Robots and Systems , pages 5026–5033, 2012.
[28] Yunhai Han, Mandy Xie, Ye Zhao, and Harish Ravichan-
dar. On the utility of koopman operator theory in learning
dexterous manipulation skills. In Conference on Robot
Learning, pages 106–126. PMLR, 2023.
[29] Hongyi Chen, Abulikemu Abuduweili, Aviral Agrawal,
Yunhai Han, Harish Ravichandar, Changliu Liu, and Jef-
frey Ichnowski. KOROL: Learning Visualizable Object
Feature with Koopman Operator Rollout for Manipu-
lation, September 2024. URL http://arxiv.org/abs/2407.
00548. arXiv:2407.00548 [cs].
[30] Peter Henderson, Riashat Islam, Philip Bachman, Joelle
Pineau, Doina Precup, and David Meger. Deep reinforce-
ment learning that matters. In Proceedings of the AAAI
conference on artificial intelligence , 2018.
[31] Yunhai Han, Zhenyang Chen, Kyle A Williams, and
Harish Ravichandar. Learning prehensile dexterity by
imitating and emulating state-only observations. IEEE
Robotics and Automation Letters , 2024.
[32] Laurens van der Maaten and Geoffrey Hinton. Visu-
alizing data using t-sne. Journal of machine learning
research, 9(Nov):2579–2605, 2008.
[33] Nicolas Carion, Laura Gustafson, Yuan-Ting Hu, Shoub-
hik Debnath, Ronghang Hu, Didac Suris, Chaitanya
Ryali, Kalyan Vasudev Alwala, Haitham Khedr, Andrew
Huang, et al. Sam 3: Segment anything with concepts.
arXiv preprint arXiv:2511.16719 , 2025.
