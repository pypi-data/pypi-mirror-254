; ModuleID = 'qat-link'
source_filename = "qat-link"

%Array = type opaque
%Qubit = type opaque
%Result = type opaque

define void @TeleportChain__DemonstrateTeleportationUsingPresharedEntanglement__Interop() local_unnamed_addr #0 {
entry:
  br label %quantum19

quantum19:                                        ; preds = %entry
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Result* null)
  tail call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %readout18

readout18:                                        ; preds = %quantum19
  %0 = tail call i1 @__quantum__qis__read_result__body(%Result* null)
  br label %post-classical17

post-classical17:                                 ; preds = %readout18
  br label %exit_quantum_grouping20

exit_quantum_grouping20:                          ; preds = %post-classical17
  br i1 %0, label %then0__1.i.i.i, label %continue__1.i.i.i

then0__1.i.i.i:                                   ; preds = %exit_quantum_grouping20
  br label %quantum

quantum:                                          ; preds = %then0__1.i.i.i
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  br label %readout

readout:                                          ; preds = %quantum
  br label %post-classical

post-classical:                                   ; preds = %readout
  br label %exit_quantum_grouping

exit_quantum_grouping:                            ; preds = %post-classical
  br label %continue__1.i.i.i

continue__1.i.i.i:                                ; preds = %exit_quantum_grouping20, %exit_quantum_grouping
  br label %quantum23

quantum23:                                        ; preds = %continue__1.i.i.i
  tail call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Result* nonnull inttoptr (i64 1 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  br label %readout22

readout22:                                        ; preds = %quantum23
  %1 = tail call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 1 to %Result*))
  br label %post-classical21

post-classical21:                                 ; preds = %readout22
  br label %exit_quantum_grouping24

exit_quantum_grouping24:                          ; preds = %post-classical21
  br i1 %1, label %then0__2.i.i.i, label %TeleportChain__TeleportQubitUsingPresharedEntanglement__body.2.exit.i

then0__2.i.i.i:                                   ; preds = %exit_quantum_grouping24
  br label %quantum3

quantum3:                                         ; preds = %then0__2.i.i.i
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  br label %readout2

readout2:                                         ; preds = %quantum3
  br label %post-classical1

post-classical1:                                  ; preds = %readout2
  br label %exit_quantum_grouping4

exit_quantum_grouping4:                           ; preds = %post-classical1
  br label %TeleportChain__TeleportQubitUsingPresharedEntanglement__body.2.exit.i

TeleportChain__TeleportQubitUsingPresharedEntanglement__body.2.exit.i: ; preds = %exit_quantum_grouping24, %exit_quantum_grouping4
  br label %quantum27

quantum27:                                        ; preds = %TeleportChain__TeleportQubitUsingPresharedEntanglement__body.2.exit.i
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Result* nonnull inttoptr (i64 2 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  br label %readout26

readout26:                                        ; preds = %quantum27
  %2 = tail call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 2 to %Result*))
  br label %post-classical25

post-classical25:                                 ; preds = %readout26
  br label %exit_quantum_grouping28

exit_quantum_grouping28:                          ; preds = %post-classical25
  br i1 %2, label %then0__1.i.i1.i, label %continue__1.i.i2.i

then0__1.i.i1.i:                                  ; preds = %exit_quantum_grouping28
  br label %quantum7

quantum7:                                         ; preds = %then0__1.i.i1.i
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  br label %readout6

readout6:                                         ; preds = %quantum7
  br label %post-classical5

post-classical5:                                  ; preds = %readout6
  br label %exit_quantum_grouping8

exit_quantum_grouping8:                           ; preds = %post-classical5
  br label %continue__1.i.i2.i

continue__1.i.i2.i:                               ; preds = %exit_quantum_grouping28, %exit_quantum_grouping8
  br label %quantum31

quantum31:                                        ; preds = %continue__1.i.i2.i
  tail call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Result* nonnull inttoptr (i64 3 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  br label %readout30

readout30:                                        ; preds = %quantum31
  %3 = tail call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 3 to %Result*))
  br label %post-classical29

post-classical29:                                 ; preds = %readout30
  br label %exit_quantum_grouping32

exit_quantum_grouping32:                          ; preds = %post-classical29
  br i1 %3, label %then0__2.i.i3.i, label %TeleportChain__DemonstrateTeleportationUsingPresharedEntanglement__body.1.exit

then0__2.i.i3.i:                                  ; preds = %exit_quantum_grouping32
  br label %quantum11

quantum11:                                        ; preds = %then0__2.i.i3.i
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  br label %readout10

readout10:                                        ; preds = %quantum11
  br label %post-classical9

post-classical9:                                  ; preds = %readout10
  br label %exit_quantum_grouping12

exit_quantum_grouping12:                          ; preds = %post-classical9
  br label %TeleportChain__DemonstrateTeleportationUsingPresharedEntanglement__body.1.exit

TeleportChain__DemonstrateTeleportationUsingPresharedEntanglement__body.1.exit: ; preds = %exit_quantum_grouping12, %exit_quantum_grouping32
  br label %quantum15

quantum15:                                        ; preds = %TeleportChain__DemonstrateTeleportationUsingPresharedEntanglement__body.1.exit
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 4 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  tail call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Result* nonnull inttoptr (i64 5 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  br label %readout14

readout14:                                        ; preds = %quantum15
  br label %post-classical13

post-classical13:                                 ; preds = %readout14
  br label %exit_quantum_grouping16

exit_quantum_grouping16:                          ; preds = %post-classical13
  ret void
}

declare void @__quantum__rt__array_update_alias_count(%Array*, i32) local_unnamed_addr

declare void @__quantum__qis__reset__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__x__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__z__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__h__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__cnot__body(%Qubit*, %Qubit*) local_unnamed_addr

declare void @__quantum__qis__mz__body(%Qubit*, %Result*) local_unnamed_addr

declare i1 @__quantum__qis__read_result__body(%Result*) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="6" "requiredResults"="6" }

